from scraper_bot import Scraper, FormFiller
from config import (
    ZILLOW_URL,
    REQUEST_HEADERS,
    GOOGLE_FORM_URL,
)

def main():
    # Create the scraper bot
    scraper = Scraper(ZILLOW_URL, REQUEST_HEADERS)

    # Get the list of apartments
    apartments_list = scraper.run()
    apartments_number = len(apartments_list)

    print(f"🔍 Found {apartments_number} apartments!\n")

    # Create filler bot
    filler = FormFiller(url=GOOGLE_FORM_URL)

    # Start looping through apartments
    form_filled = 0
    print(f"📝 Target: {apartments_number} submissions!\n")
    print("." * apartments_number)

    for apartment in apartments_list:
        all_items_filled = filler.fill_form(apartment)
        if all_items_filled:
            form_filled += 1
            print(".", end="", flush=True)

    print(f"\n\n🏠 Successfully filled {form_filled}/{apartments_number} apartments in the form!")

if __name__ == '__main__':
    main()
