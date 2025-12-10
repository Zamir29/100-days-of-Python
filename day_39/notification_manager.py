from twilio.rest import Client
from config import (
    TWILIO_SID,
    TWILIO_TOKEN,
    TWILIO_WHATSAPP_FROM,
    TWILIO_WHATSAPP_TO,
)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.from_number = TWILIO_WHATSAPP_FROM
        self.to_number = TWILIO_WHATSAPP_TO

    def send_notification(self, content):

        body = (
            f"🚨Low price alert\n"
            f"Only *€{content.price:2f}* to fly "
            f"from {content.departure_code} "
            f"to {content.arrival_code} "
            f"on {content.departure_date}\n"
            f"[search window {deal.start_date} → {deal.end_date}]"
        )

        message = self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body= body,
        )

        return message.sid