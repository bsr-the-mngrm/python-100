import os
from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        load_dotenv()
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_phone_number = os.getenv('FROM_PHONE_NUMBER')
        self.to_phone_number = os.getenv('TO_PHONE_NUMBER')

    def send_sms(self, flight: FlightData):
        client = Client(self.account_sid, self.auth_token)

        msg = flight.sms_message()

        message = client.messages \
            .create(
                body=msg,
                from_=self.from_phone_number,
                to=self.to_phone_number
            )
