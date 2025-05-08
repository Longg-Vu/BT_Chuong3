# Bài tập chương 3


# Tự động sao lưu database và gửi email thông báo

Đây là một chương trình Python giúp tự động sao lưu các tệp database (.sql, .sqlite3) từ thư mục \data/\ vào thư mục \backup/\ mỗi ngày lúc 00:00, đồng thời gửi email thông báo về quá trình sao lưu (thành công hoặc thất bại).

## Cấu hình

1. **Cài đặt môi trường**
   
Cài đặt Python và các thư viện cần thiết bằng cách sử dụng file \
equirements.txt\.

2. **Tạo file \.env\**
   
   Để cấu hình email, tạo một file \.env\ trong cùng thư mục với mã nguồn và điền thông tin sau:

   \\\
   SENDER_EMAIL=your_email@gmail.com
   APP_PASSWORD=your_app_password
   RECEIVER_EMAIL=receiver_email@example.com
   \\\

   - \SENDER_EMAIL\: Email của bạn dùng để gửi email thông báo.
   - \APP_PASSWORD\: Mật khẩu ứng dụng của bạn (có thể tạo trên Gmail).
   - \RECEIVER_EMAIL\: Email nhận thông báo.

3. **Cài đặt thư viện cần thiết**

   Chạy lệnh sau để cài đặt các thư viện phụ thuộc:
   pip install -r requirements.txt

4. **Cấu hình thư mục**

   - **\data/\**: Chứa các file database cần sao lưu (tệp có đuôi \.sql\ hoặc \.sqlite3\).
   - **\backup/\**: Chứa các bản sao lưu của các file từ thư mục \data/\.

## Chạy chương trình

Chạy chương trình bằng cách sử dụng lệnh sau:

python backup_script.py

Chương trình sẽ tự động sao lưu các file và gửi email thông báo hàng ngày vào lúc 00:00.

## Các chức năng

- **Sao lưu tự động**: Chương trình sao lưu các file có đuôi \.sql\ hoặc \.sqlite3\ từ thư mục \data/\ vào thư mục \ackup/\ mỗi ngày.
- **Thông báo qua email**: Gửi email thông báo về quá trình sao lưu (thành công hoặc thất bại).

## Thư viện yêu cầu

- \schedule\: Để lập lịch sao lưu.
- \smtplib\: Để gửi email thông qua SMTP.
- \shutil\: Để sao chép file.
- \dotenv\: Để đọc cấu hình từ file \.env\.
- \	ime\: Để tạo độ trễ trong vòng lặp.

## Lưu ý

- Đảm bảo rằng bạn đã bật quyền truy cập ứng dụng kém an toàn nếu sử dụng Gmail.
- Đảm bảo rằng thư mục \data/\ và \backup/\ tồn tại trước khi chạy chương trình.
