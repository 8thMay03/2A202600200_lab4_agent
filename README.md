# TravelBuddy - Lab4 Agent

TravelBuddy là chatbot tư vấn du lịch tiếng Việt, dùng LangGraph + OpenAI + tool calling.
Project mô phỏng 3 nghiệp vụ chính:

- Tra cứu chuyến bay (`search_flights`)
- Tra cứu khách sạn (`search_hotels`)
- Tính ngân sách còn lại (`calculate_budget`)

## Mục tiêu bài lab

- Xây dựng agent có system prompt theo XML.
- Dùng tools để trả lời câu hỏi du lịch theo ngữ cảnh.
- Thể hiện luồng multi-step (flight -> hotel -> budget).
- Có guardrail từ chối yêu cầu ngoài phạm vi du lịch.

## Cấu trúc thư mục

- `src/agent.py`: entrypoint chạy chat CLI và xây graph.
- `src/tools.py`: dữ liệu mẫu + implement 3 tools.
- `src/system_prompt.txt`: prompt hệ thống cho persona/rules/constraints.
- `src/testcase`: 5 test case yêu cầu của bài.
- `src/test_results.md`: kết quả chạy test thủ công.

## Yêu cầu môi trường

- Python 3.10+
- OpenAI API key hợp lệ

## Cài đặt

Từ thư mục gốc project:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install langchain-openai langgraph langchain-core python-dotenv typing-extensions
```

Tạo file `.env` (ở root):

```env
OPENAI_API_KEY=your_api_key_here
```

## Chạy chương trình

Do `agent.py` import `tools.py` cùng thư mục, hãy chạy từ `src`:

```bash
cd src
python agent.py
```

Thoát bằng `quit` / `exit` / `q`.

## Luồng hoạt động

1. `agent.py` đọc `system_prompt.txt`.
2. Khởi tạo `ChatOpenAI` và bind 3 tools.
3. Dựng `StateGraph` với 2 node:
   - `agent`: gọi LLM, quyết định có gọi tool không
   - `tools`: thực thi tool call từ agent
4. Graph loop:
   - `START -> agent`
   - nếu có tool call thì `agent -> tools -> agent`
   - nếu không có tool call thì kết thúc và in câu trả lời.

## Logic tools

### `search_flights(origin, destination)`

- Tra theo key tuple `(origin, destination)` trong `FLIGHTS_DB`.
- Nếu không có, thử tra ngược `(destination, origin)`.
- Trả danh sách chuyến bay đã format giá VND (`1.450.000đ`).

### `search_hotels(city, max_price_per_night)`

- Lấy dữ liệu từ `HOTELS_DB[city]`.
- Lọc theo giá tối đa mỗi đêm.
- Sắp xếp theo `rating` giảm dần.
- Trả list khách sạn hoặc thông báo không có kết quả.

### `calculate_budget(total_budget, expenses)`

- Parse `expenses` dạng: `ten_khoan:so_tien,ten_khoan:so_tien`.
- Tính tổng chi và số tiền còn lại.
- Trả bảng chi tiết chi phí + cảnh báo nếu vượt ngân sách.
- Có validate và trả lỗi rõ ràng nếu format sai.

## Cơ chế ép gọi `calculate_budget` (Test 3)

Trong `agent.py` có guard logic để ép multi-step:

- Nếu user có nhắc `budget/ngân sách/triệu`
- Và đã có call `search_flights` + `search_hotels`
- Nhưng model chưa gọi `calculate_budget`

=> Agent sẽ tự tạo tool call `calculate_budget` để bắt buộc chạy qua `ToolNode`.

Mục đích: đảm bảo test case chuỗi tool luôn có bước tính ngân sách.

## Test nhanh

Tham khảo file `src/testcase` với 5 kịch bản:

- Direct answer không cần tool
- Single tool call
- Multi-step tool chaining
- Clarification khi thiếu thông tin
- Guardrail từ chối yêu cầu ngoài domain

## Hạn chế hiện tại

- Dữ liệu flights/hotels là dữ liệu mock (hard-coded), không realtime.
- Parse ngân sách/số đêm bằng regex đơn giản, chưa bao phủ mọi cách diễn đạt.
- Chưa có test unit tự động; chủ yếu test manual qua CLI.

## Gợi ý mở rộng

- Thêm test tự động cho từng tool và cho graph flow.
- Chuẩn hóa parser tiếng Việt (ngân sách, ngày đi, số đêm) robust hơn.
- Kết nối API thật cho vé máy bay/khách sạn.
- Thêm memory ngắn hạn theo phiên chat.
