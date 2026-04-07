from pathlib import Path
import re
from typing import Annotated
from uuid import uuid4

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict

from tools import calculate_budget, search_flights, search_hotels

load_dotenv()

# 1. Đọc System Prompt
SYSTEM_PROMPT_PATH = Path(__file__).with_name("system_prompt.txt")
with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


# 2. Khai báo State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)


def _extract_budget_vnd(text: str) -> int | None:
    lowered = text.lower()
    m = re.search(r"(\d+)\s*triệu", lowered)
    if m:
        return int(m.group(1)) * 1_000_000
    m = re.search(r"(\d[\d\.]*)", lowered)
    if m:
        return int(m.group(1).replace(".", ""))
    return None


def _extract_nights(text: str) -> int:
    m = re.search(r"(\d+)\s*đêm", text.lower())
    return int(m.group(1)) if m else 1


def _extract_prices_from_tool_output(text: str) -> list[int]:
    prices: list[int] = []
    for raw in re.findall(r"(\d[\d\.]*)đ", text):
        prices.append(int(raw.replace(".", "")))
    return prices


def _should_force_budget(messages: list) -> bool:
    has_flights = False
    has_hotels = False
    has_budget_call = False
    latest_user_text = ""

    for msg in messages:
        if isinstance(msg, HumanMessage):
            latest_user_text = msg.content if isinstance(msg.content, str) else ""
        if isinstance(msg, AIMessage):
            for tc in (msg.tool_calls or []):
                name = tc.get("name")
                if name == "search_flights":
                    has_flights = True
                elif name == "search_hotels":
                    has_hotels = True
                elif name == "calculate_budget":
                    has_budget_call = True
        if isinstance(msg, ToolMessage) and msg.name == "calculate_budget":
            has_budget_call = True

    wants_budget = any(
        k in latest_user_text.lower() for k in ("budget", "ngân sách", "triệu")
    )
    return wants_budget and has_flights and has_hotels and not has_budget_call


def _build_forced_budget_tool_call(messages: list) -> AIMessage | None:
    latest_user_text = ""
    flight_prices: list[int] = []
    hotel_prices: list[int] = []

    for msg in messages:
        if isinstance(msg, HumanMessage):
            latest_user_text = msg.content if isinstance(msg.content, str) else ""
        if isinstance(msg, ToolMessage) and isinstance(msg.content, str):
            if msg.name == "search_flights":
                flight_prices.extend(_extract_prices_from_tool_output(msg.content))
            elif msg.name == "search_hotels":
                # search_hotels có giá theo /đêm
                hotel_prices.extend(_extract_prices_from_tool_output(msg.content))

    total_budget = _extract_budget_vnd(latest_user_text)
    if total_budget is None:
        return None

    if not flight_prices or not hotel_prices:
        return None

    nights = _extract_nights(latest_user_text)
    cheapest_flight = min(flight_prices)
    cheapest_hotel_total = min(hotel_prices) * nights
    expenses = f"ve_bay:{cheapest_flight},khach_san:{cheapest_hotel_total}"

    forced_call = {
        "name": "calculate_budget",
        "args": {"total_budget": total_budget, "expenses": expenses},
        "id": f"call_{uuid4().hex[:8]}",
        "type": "tool_call",
    }
    return AIMessage(content="", tool_calls=[forced_call])


# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = llm_with_tools.invoke(messages)

    # Ép cứng: nếu user có ngân sách và đã có flights + hotels nhưng model chưa gọi budget,
    # thì tạo tool call calculate_budget bắt buộc chạy qua ToolNode.
    if not response.tool_calls and _should_force_budget(messages):
        forced = _build_forced_budget_tool_call(messages)
        if forced is not None:
            response = forced

    # === LOGGING ===
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"[Gọi tool: {tc['name']}]({tc['args']})")
    else:
        print("[Trả lời trực tiếp]")

    return {"messages": [response]}


# 5. Xây dựng Graph
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()


# 6. Chat loop
if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý Du lịch Thông minh")
    print("   Gõ 'quit' để thoát")
    print("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break

        print("\nTravelBuddy đang suy nghĩ...")
        result = graph.invoke({"messages": [("human", user_input)]})
        final = result["messages"][-1]
        print(f"\nTravelBuddy: {final.content}")