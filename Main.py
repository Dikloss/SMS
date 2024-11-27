import smtplib
from email.message import EmailMessage

sender_email = "ororlovv@mail.ru"
recipient_mail = "ismdag@mail.ru"
password = "F8cRM4iEk01YBWv1itCS"
subject = "Проверка связи"
body = "Привет из программы на Питоне"

msg = EmailMessage()
msg.set_content(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_mail

try:
    server = smtplib.SMTP_SSL("smtp.mail.ru", )
    server.login(sender_email, password)
    server.send_message(msg)
    print("Письмо отправлено")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    if server:
        server.quit()
