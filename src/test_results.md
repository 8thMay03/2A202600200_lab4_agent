**Testcase 1 - Direct Answer (Không cần tool)**

Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa
 biết đi đâu

TravelBuddy đang suy nghĩ...
[Trả lời trực tiếp]

TravelBuddy: Chào bạn! Thật tuyệt khi có kế hoạch du lịch! Bạn có một số điểm đến yêu thích nào không, hay bạn cần gợi ý? Nếu được, cho mdu lịch! Bạn có một số điểm đến yêu thích nào không, hay bạn cần gợi ý? Nếu được, cho mình biết một số thông tin như ngày đi, số người, và ngân sách để mình có thể tư vấn tốt hơn nhé!

============================================================  
**Testcase 2 - Single Tool Call**  
Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
[Gọi tool: search_flights]({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
[Trả lời trực tiếp]

TravelBuddy: Chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines**
  - Giờ bay: 06:00–07:20 
  - Giá vé: 1.450.000đ 
  - Hạng: Economy
2. **Vietnam Airlines**
  - Giờ bay: 14:00–15:20 
  - Giá vé: 2.800.000đ 
  - Hạng: Business
3. **VietJet Air**
  - Giờ bay: 08:30–09:50 
  - Giá vé: 890.000đ 
  - Hạng: Economy
4. **Bamboo Airways**
  - Giờ bay: 11:00–12:20 
  - Giá vé: 1.200.000đ 
  - Hạng: Economy

Nếu bạn cần thêm thông tin khác hoặc muốn đặt vé, hãy cho tôi biết nhé!

============================================================  
**Testcase 3 - Multi-step Tool Chaining**  
Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...
[Gọi tool: search_flights]({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
[Gọi tool: search_hotels]({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
[Trả lời trực tiếp]

TravelBuddy: Dưới đây là gợi ý cho chuyến đi từ Hà Nội đến Phú Quốc 2 đêm với ngân sách 5 triệu đồng:

**Chuyến bay:**  

1. **Vietnam Airlines**: 07:00–09:15 | 2.100.000đ (hạng economy)
2. **VietJet Air**: 10:00–12:15 | 1.350.000đ (hạng economy)
3. **VietJet Air**: 16:00–18:15 | 1.000.000đ (hạng economy)

**Khách sạn:**  

1. **9Station Hostel**: 2 sao | 200.000đ/đêm | Dương Đông | rating 4.5
2. **Sol by Meliá**: 4 sao | 1.500.000đ/đêm | Bãi Trường | rating 4.2
3. **Lahana Resort**: 3 sao | 800.000đ/đêm | Dương Đông | rating 4.0

**Tổng chi phí ước tính:**

- Nếu chọn chuyến bay giá rẻ nhất (VietJet Air 1.000.000đ) và ở lại 9Station Hostel (200.000đ/đêm):
  - Vé máy bay: 1.000.000đ
  - Khách sạn: 200.000đ x 2 đêm = 400.000đ
  - **Tổng cộng: 1.400.000đ**
- Nếu chọn chuyến bay của Vietnam Airlines (2.100.000đ) và ở Sol by Meliá (1.500.000đ/đêm):
  - Vé máy bay: 2.100.000đ
  - Khách sạn: 1.500.000đ x 2 đêm = 3.000.000đ
  - **Tổng cộng: 5.100.000đ** (vượt ngân sách)

Vậy, nếu bạn muốn tiết kiệm, phương án bay VietJet và ở hostel là hợp lý nhất!

**Gợi ý thêm:** Hãy cân nhắc đặt phòng và vé máy bay sớm để đảm bảo không hết chỗ nhé!

============================================================  
**Testcase 4 - Missing Info / Clarification**  
Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
[Trả lời trực tiếp]

TravelBuddy: Thông tin cần bổ sung: Bạn muốn đặt khách sạn ở thành phố nào, ngân sách tối đa mỗi đêm là bao nhiêu và thời gian lưu trú khoảng bao lâu?

============================================================  
**Testcase 5 - Guardrail / Refusal**  
Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
[Trả lời trực tiếp]

TravelBuddy: Mình không thể giúp bạn với yêu cầu về lập trình. Nhưng nếu bạn có thể cho mình biết rõ hơn về chuyến đi của bạn, mình sẽ hỗ trợ bạn lên kế hoạch du lịch tốt nhất nhé! Hãy cho mình biết bạn đang dự định đi đâu, khi nào và ngân sách khoảng bao nhiêu nhé!