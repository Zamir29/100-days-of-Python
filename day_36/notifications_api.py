from twilio.rest import Client

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
            message = client.messages.create(
                from_=self.from_number,
                to=self.to_number,
                media_url=item["media"],
                body=body
            )

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