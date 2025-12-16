from datetime import datetime
TODAY = datetime.today()
TODAY_YEAR = TODAY.year
START_YEAR = 1900

def check_date(input_date):
    scraping_date = input_date
    while True:
        try:
            # Split string by -
            checking_date = scraping_date.split("-")

            # Check if there are three items
            if len(checking_date) != 3:
                raise ValueError("Format is not valid!")

            # Check if the numbers are not letters
            for num in checking_date:
                if not num.isdigit():
                    raise ValueError(f"'{num}' is not a number!")

            # Map every item as an int
            year, month, day = map(int, checking_date)

            # Check if year is within the range
            if not (START_YEAR <= year <= TODAY_YEAR):
                raise ValueError(f"Please enter a year above {START_YEAR} and below {TODAY_YEAR}.")

            try:
                # Check if date is a calendar valid date
                datetime(year=year, month=month, day=day)

                return scraping_date

            except ValueError:
                    raise ValueError("The date you entered does not exist!")


        except ValueError as error:
            print(error)
            scraping_date = input("Please enter a year in the format YYYY-MM-DD: ")

def main():
    scraping_date = input("What year would you like to travel?\nType in this format YYYY-MM-DD: ")
    scraping_date = check_date(scraping_date)
    print(f"Using scraping date: {scraping_date}")
if __name__ == '__main__':
    main()
