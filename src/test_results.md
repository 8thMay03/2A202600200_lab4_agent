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
[Gọi tool: calculate_budget]({'total_budget': 5000000, 'expenses': 've_bay:1000000,khach_san:400000'})
[Trả lời trực tiếp]

TravelBuddy: Chuyến đi Phú Quốc của bạn sẽ như thế này:

**Chuyến bay:**

1. VietJet Air | 16:00 - 18:15 | 1.000.000đ | hạng economy
2. Hoặc bạn có thể chọn chuyến bay vào 10:00 - 12:15 với giá 1.350.000đ.

**Khách sạn:**

1. **9Station Hostel** | 2 sao | 200.000đ/đêm | Dương Đông | rating 4.5
2. **Lahana Resort** | 3 sao | 800.000đ/đêm | Dương Đông | rating 4.0
3. **Sol by Meliá** | 4 sao | 1.500.000đ/đêm | Bãi Trường | rating 4.2

Giả sử bạn ở 2 đêm tại **9Station Hostel**:

- Chi phí vé máy bay: 1.000.000đ
- Chi phí khách sạn (2 đêm): 400.000đ

**Tổng chi phí ước tính: 1.400.000đ**

**Số tiền còn lại trong ngân sách: 3.600.000đ.**

**Gợi ý thêm:**

- Sử dụng số tiền còn lại để tham gia các tour, ăn uống, hoặc trải nghiệm các hoạt động tại Phú Quốc (như lặn biển, tham quan các hòn đảo xung quanh).
- Bạn có thể tham khảo các nhà hàng và quán ăn địa phương để thưởng thức món hải sản tươi ngon!

Nếu bạn có thêm câu hỏi hoặc cần giúp đỡ gì khác, cứ hỏi nhé!

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