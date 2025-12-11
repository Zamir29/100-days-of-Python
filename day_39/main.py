from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

DEPARTURE_CITY_CODE = "MIL" # This can be an input request from the user


# Helpers
def ensure_iata_code(row: dict, flight_search: FlightSearch, data_manager: DataManager) -> str:
    """
    Ensure the row has an IATA code.
    - If it's missing, fetch it from Amadeus and update the sheet.
    - Return the IATA code to the caller.
    :param row: the dict from Sheety API
    :param flight_search: class from FlightSearch
    :param data_manager: class from DataManager
    :return: IATA code as string
    """
    if not row["iataCode"]:
        iata = flight_search.get_iata_code(city_name=row["city"])
        row["iataCode"] = iata
        data_manager.update_row(row_id=row["id"], updates={"iataCode": iata})
    return row["iataCode"]

def send_alert_if_deal(
        row: dict,
        departure_city_code: str,
        flight_search: FlightSearch,
        notifier: NotificationManager,
) -> str:
    """
    For given destination row:
    - Find the best flight deal from DEPARTURE_CITY_CODE.
    - Send a notification if a deal is found.
    - Return the Twilio message SID.
    May raise ValueError if no deal matches the threshold.
    :param row: row from Sheety API
    :param departure_city_code: constant given by the user
    :param flight_search: class of FlightSearch
    :param notifier: class of NotificationManager
    :return: Returns message_id (SID)
    """
    best_deal = flight_search.find_deals(
        origin_code=departure_city_code,
        destination_code=row["iataCode"],
        max_price=float(row["lowestPrice"]),
    )

    message_sid = notifier.send_notification(content=best_deal)
    return message_sid

def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notifier = NotificationManager()

    # Get the row from the table on Google Sheet
    try:
        rows, _ = data_manager.get_table()
    except ValueError as error:
        print(f"Fatal {error}")
        return

    # For each row check if there is any field empty to fill.
    for row in rows:
        # Try to check on Amadeus, gathering the ValueError in each method and print it
        try:
            # First check if an Iata Code is present for the row
            ensure_iata_code(row, flight_search, data_manager)

            # Try to find a deal and send an alert
            message_id = send_alert_if_deal(
                row=row,
                departure_city_code=DEPARTURE_CITY_CODE,
                flight_search=flight_search,
                notifier=notifier,
            )

            print(f"Alert sent for {row['city']} - Twilio SID: {message_id}")

        except ValueError as error_message:
            # The ValueError in each step of any method will be printed and will skip this destination
            print(f"Skipping destination: {error_message}")
            continue

if __name__ == "__main__":
    main()