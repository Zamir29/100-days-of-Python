from twilio.rest import Client
import time

class SendNotifications:

    def __init__(self, tw_sid, tw_token, from_n, to_n, messages_container, ticker, sign, percentage):
        """
        Send notifications in separated messages based on the number of messages present message_container
        :param tw_sid: Twilio_SID
        :param tw_token: Twilio_token
        :param from_n:
        :param to_n:
        :param messages_container: This is a list of dictionaries
        :param ticker: Stock ticker symbol, e.g. 'TSLA'
        :param sign: '🔺' or '🔻'
        :param percentage: numeric percentage move
        """
        self.tw_sid = tw_sid
        self.tw_token = tw_token
        self.from_number = from_n
        self.to_number = to_n
        self.message_container = messages_container
        self.ticker = ticker
        self.sign = sign
        self.percentage_value = round(percentage, 2)

    def send_notification(self):
        """
        Take any message and build the body to send to the number defined with to_n
        """
        account_sid = self.tw_sid
        auth_token = self.tw_token
        client = Client(account_sid, auth_token)

        for item in self.message_container:
            body = self.build_body(article=item)

            media = item.get("media")
            media_url = None
            if media and not media.lower().endswith(".webp"):
                media_url = media

            message = client.messages.create(
                from_=self.from_number,
                to=self.to_number,
                media_url=media_url,
                body=body,
            )
            print("Sent message SID:", message.sid)
            time.sleep(2)

    def build_body(self, article):
        """
        Takes the article and returns a body formatted with all the data
        """
        body = (f"*{self.ticker}*: {self.sign}{self.percentage_value}%\n\n"
                f"*Headline*: {article['headline']}\n"
                f"*Brief*: {article['brief']}\n"
                f"____\n"
                f"*Link*: {article['url']}\n"
                f"*Date*: ```{article['date']}```")

        return body

    # Alternative to make the images always work:
    import requests

    # def is_supported_image(url: str) -> bool:
    #     try:
    #         resp = requests.head(url, timeout=5)
    #         content_type = resp.headers.get("Content-Type", "").lower()
    #         # Allow jpeg / png / gif, block webp
    #         return (
    #                 content_type.startswith("image/")
    #                 and "webp" not in content_type
    #         )
    #     except Exception:
    #         # If we can't tell, be conservative and skip
    #         return False

    # media = item.get("media")
    # media_url = None
    # if media and is_supported_image(media):
    #     media_url = media