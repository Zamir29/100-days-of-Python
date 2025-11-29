import os
from stock_api import StockAPI

STOCK = "TSLA"

def main():
    api_key = os.getenv("AV_API_KEY")
    print(f"API key loaded? {api_key is not None}")

    stock = StockAPI(
        api_key=api_key,
        ticker=STOCK,
    )

    last_close, prev_close = stock.get_closing_prices()

    print(f"Last close: {last_close}")
    print(f"Previous close: {prev_close}")

main()