from scraper_bot import Scraper, FormFiller
from config import (
    ZILLOW_URL,
    REQUEST_HEADERS,
    GOOGLE_FORM_URL,
)

scraper = Scraper(url=ZILLOW_URL, headers=REQUEST_HEADERS)

apartments_list = scraper.run()

just_one = apartments_list[0]
print(just_one)

filler_bot = FormFiller(url=GOOGLE_FORM_URL)


filler_bot.fill_form(just_one)
