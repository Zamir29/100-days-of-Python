import os
from stock_api import StockAPI
from news_api import NewsAPI
from notifications_api import SendNotifications

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD=1 # insert the integer, e.g. 5% -> 5

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock = StockAPI(
    api_key= os.getenv("AV_API_KEY"),
    ticker=STOCK,
)

last_close, prev_close, prev_date = stock.get_closing_prices()

sign, percentage = stock.get_diff(price_now=last_close, price_prev=prev_close)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news = NewsAPI(
    api_key=os.getenv("NEWS_API"),
    query=COMPANY_NAME,
    from_date=prev_date
)

if percentage >= THRESHOLD:
    show_articles = news.get_news()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    notifier = SendNotifications(
        tw_sid=os.getenv("TWILIO_SID"),
        tw_token=os.getenv("TWILIO_TOKEN"),
        from_n=os.getenv("TWILIO_WHATSAPP_FROM"),
        to_n=os.getenv("TWILIO_WHATSAPP_TO"),
        messages_container=show_articles,
        ticker=STOCK,
        sign=sign,
        percentage=percentage,

    )

    notifier.send_notification()

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

