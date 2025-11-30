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

    # Sanity check for get_diff
    stock_up = stock.get_diff(110, 100)
    stock_down = stock.get_diff(90, 110)

    print(f"\nTest the get_diff with:\nStock down: {stock_down}\nStock up: {stock_up}\n")

    stock_real = stock.get_diff(price_now=last_close, price_prev=prev_close)

    print(f"The stock of \"{STOCK}\" registered  {stock_real[0]}{round(stock_real[1])}%")

if __name__ == "__main__":
    main()
