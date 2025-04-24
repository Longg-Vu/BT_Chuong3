import os
import shutil
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

# Lấy thông tin từ file .env
load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

DATA_FOLDER = "data"
BACKUP_FOLDER = "backup"

def send_mail(subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f"Gửi email thành công đến {receiver_email}!")
    except Exception as e:
        print(f"Gửi email thất bại. Lỗi: {e}")

def backup_files():
    try:
        os.makedirs(BACKUP_FOLDER, exist_ok=True)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        found = False

        for file in os.listdir(DATA_FOLDER):
            if file.endswith(".sql") or file.endswith(".sqlite3"):
                src = os.path.join(DATA_FOLDER, file)
                dst = os.path.join(BACKUP_FOLDER, f"{now}_{file}")
                shutil.copy2(src, dst)
                found = True

        if found:
            send_mail("Backup thành công", f"Backup hoàn tất lúc {now}.")
        else:
            send_mail("Không tìm thấy file database", f"Không có file .sql hoặc .sqlite3 lúc {now}.")
    except Exception as e:
        send_mail("Backup thất bại", f"Lỗi xảy ra: {e}")


schedule.every().day.at("00:00").do(backup_files)

print("Đang chờ tới 00:00 để thực hiện backup...")
while True:
    schedule.run_pending()
    time.sleep(60)
