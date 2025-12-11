from twilio.rest import Client
from config import (
    TWILIO_SID,
    TWILIO_TOKEN,
    TWILIO_WHATSAPP_FROM,
    TWILIO_WHATSAPP_TO,
)
from day_39.flight_data import FlightData


class NotificationManager:
    """Handles sending flight deal alerts to the user.

    This class wraps Twilio so the rest of the codebase only needs to pass
    a `FlightData` instance and doesn’t care about Twilio’s API details.

    Attributes:
        client (Client): Authenticated Twilio client used to send messages.
        from_number (str): Twilio phone number / WhatsApp sender used
            as the message origin.
        to_number (str): Destination phone number / WhatsApp recipient
            for the alerts.
    """
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.from_number = TWILIO_WHATSAPP_FROM
        self.to_number = TWILIO_WHATSAPP_TO

    def send_notification(self, content: FlightData) -> str:
        """Send a low-price alert for the given flight deal.

        Formats a human-readable message from the `FlightData` fields and
        sends it via Twilio (SMS or WhatsApp, depending on your config).

        Args:
            content: A `FlightData` instance describing the best deal
                (price, IATA codes, dates, search window).

        Returns:
            str: The Twilio message SID so callers can log or inspect
            the delivery later.

        Raises:
            twilio.base.exceptions.TwilioRestException: If the Twilio API
                call fails for any reason (network, invalid credentials, etc.).
        """
        # First activate the client on https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1

        # Body is build following: https://www.twilio.com/docs/whatsapp/api#web-links-in-freeform-whatsapp-messages
        body = (
            f"🚨Low price alert\n"
            f"Only *€{content.price:.2f}* to fly "
            f"from *{content.departure_code}* "
            f"to *{content.arrival_code}* "
            f"on *{content.departure_date}*\n\n"
            f"Search window\n{content.start_date} → {content.end_date}"
        )

        message = self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body= body,
        )

        return message.sid