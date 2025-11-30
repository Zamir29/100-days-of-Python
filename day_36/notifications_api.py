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
        """
        self.tw_sid = tw_sid
        self.tw_token = tw_token
        self.from_number = from_n
        self.to_number = to_n
        self.message_container = messages_container
        self.ticker = ticker
        self.sign = sign
        self.percentage_value = percentage

    def send_notification(self):
        """
        Take any message and build the body to send to the number defined with to_n
        """
        pass

    def build_body(self):
        """
        Takes the message_container list of dictionaries and returns a body formatted with all the data
        """