import smtplib
import os
from dotenv import load_dotenv

load_dotenv('env/.env')

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_APP_KEY')
recipient_email = os.getenv('RECIPIENT_EMAIL')

connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
connection.login(user=sender_email, password=sender_password)
connection.sendmail(
    from_addr=sender_email,
    to_addrs=recipient_email,
    msg="Subject: Testing\n\nHello SMTP!"
)
connection.close()
