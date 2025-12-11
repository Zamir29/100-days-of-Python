import smtplib
from twilio.rest import Client
from config import (
    TWILIO_SID,
    TWILIO_TOKEN,
    TWILIO_WHATSAPP_FROM,
    TWILIO_WHATSAPP_TO,
    GMAIL_SMTP,
    MY_PASSWORD,
    MY_EMAIL,
)
from flight_data import FlightData

class NotificationManager:
    """
    Send flight deal alerts via Twilio (WhatsApp/SMS) and email.

    This class centralises all outbound notifications so the rest of the
    application only needs to pass a ``FlightData`` instance (and, for
    emails, a list of recipient addresses). It hides all the details of
    Twilio and SMTP configuration behind a simple Python interface.

    Attributes:
        client (Client): Authenticated Twilio client used to send WhatsApp/SMS messages.
        from_number (str): Twilio WhatsApp/SMS sender identifier (e.g. 'whatsapp:+123456789').
        to_number (str): Default Twilio recipient used for single-recipient alerts.
        gmail_smtp (str): Hostname of the SMTP server used for sending emails.
        gmail_email (str): Email address used as the sender in outgoing messages.
        gmail_password (str): App-specific password or SMTP password for ``gmail_email``.
    """
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.from_number = TWILIO_WHATSAPP_FROM
        self.to_number = TWILIO_WHATSAPP_TO
        self.gmail_smtp = GMAIL_SMTP
        self.gmail_email = MY_EMAIL
        self.gmail_password = MY_PASSWORD

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

    def send_emails(self, content: FlightData, user_emails: list[str]) -> None:
        """
        Send a flight deal email to each address in ``user_emails``.

        This method constructs a plain-text email body from the ``content``
        (price, route, departure date, and search window) and sends the
        same message to all recipients using the configured SMTP server.

        Args:
            content: The ``FlightData`` instance describing the deal that
                should be advertised in the email.
            user_emails: A list of email addresses for all subscribed customers.

        Returns:
            None. Emails are sent as a side effect.

        Raises:
            smtplib.SMTPException: If there is a problem establishing the
                SMTP connection or sending messages.
        """
        body = (
            f"🚨Low price alert\n"
            f"Only *€{content.price:.2f}* to fly "
            f"from *{content.departure_code}* "
            f"to *{content.arrival_code}* "
            f"on *{content.departure_date}*\n\n"
            f"Search window\n{content.start_date} → {content.end_date}"
        )

        if not user_emails:
            print("[INFO] No user emails found, skipping email sending.")
            return

        with smtplib.SMTP(host=self.gmail_smtp,
                          port=587,
                          timeout=30
                          ) as connection:  # adding the port number solves the idle
            connection.starttls()
            connection.login(
                user=self.gmail_email,
                password=self.gmail_password
            )
            for email in user_emails:
                connection.sendmail(
                    from_addr=self.gmail_email,
                    to_addrs=email,
                    msg=f"Subject:[Alert] Low Price from {content.departure_code} to {content.arrival_code}\n\n{body}"
                )