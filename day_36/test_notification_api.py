import os

from notifications_api import SendNotifications

def main():
    tw_sid = os.getenv("TWILIO_SID")
    tw_token = os.getenv("TWILIO_TOKEN")
    tw_from = os.getenv("TWILIO_WHATSAPP_FROM")
    tw_to = os.getenv("TWILIO_WHATSAPP_TO")

    articles = [
        {
            "headline": "TSLA jumps on strong earnings",
            "brief": "Tesla beats expectations and the stock surges.",
            "media": "https://demo.twilio.com/owl.png",
            "url": "https://example.com/tesla-news",
            "date": "2025-11-29T12:18:00Z",
        }
    ]

    notifier = SendNotifications(
        tw_sid=tw_sid,
        tw_token=tw_token,
        from_n=tw_from,
        to_n=tw_to,
        messages_container=articles,
        ticker="TSLA",
        sign="🔺",
        percentage=8.5
    )

    notifier.send_notification()

if __name__ == "__main__":
    main()