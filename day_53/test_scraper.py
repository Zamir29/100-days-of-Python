from scraper_bot import Scraper
from config import (
    ZILLOW_URL,
    REQUEST_HEADERS,
)

scraper = Scraper(url=ZILLOW_URL, headers=REQUEST_HEADERS)

ul_list = scraper.run()



print(ul_list)