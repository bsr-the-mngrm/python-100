import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        load_dotenv()
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_phone_number = os.getenv('FROM_PHONE_NUMBER')
        self.to_phone_number = os.getenv('TO_PHONE_NUMBER')
        self.email_provider_smtp_address = os.getenv('EMAIL_PROVIDER_SMTP_ADDRESS')
        self.my_email = os.getenv('MY_EMAIL')
        self.my_password = os.getenv('MY_PASSWORD')

    def send_sms(self, msg: str):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                body=msg.encode('utf-8'),
                from_=self.from_phone_number,
                to=self.to_phone_number
            )

    def send_emails(self, emails, message):
        with smtplib.SMTP(self.email_provider_smtp_address) as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            for email in emails:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
