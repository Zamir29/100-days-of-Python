from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from config import (
    SHEETY_PRICES_GET,
)

DEPARTURE_CITY_CODE = "MIL" # This can be an input request from the user


# Helpers
def ensure_iata_code(row: dict, flight_search: FlightSearch, data_manager: DataManager) -> None:
    """
    Ensure that the given destination row has an IATA city/airport code.

    If the ``iataCode`` field in ``row`` is empty, this function:
      * Uses ``flight_search`` to look up the IATA code from the ``city`` name.
      * Updates the in-memory ``row`` dict with the new code.
      * Persists the change back to the Google Sheet via ``data_manager``.

    :param row: A dictionary representing a row from the Sheety "prices" sheet
            (must contain at least ``"city"``, ``"iataCode"``, and ``"id"`` keys).
    :param flight_search: Configured FlightSearch instance used to query the Amadeus API.
    :param data_manager: Configured DataManager instance used to update the Google Sheet.
    :return: None. The function mutates ``row`` in place and updates the remote sheet
        as a side effect.

    Raises:
        ValueError: Propagated if the IATA lookup or sheet update fails.
    """
    if not row["iataCode"]:
        iata = flight_search.get_iata_code(city_name=row["city"])
        row["iataCode"] = iata
        data_manager.update_row(row_id=row["id"], updates={"iataCode": iata})

def send_alert_if_deal(best_deal_content, notifier: NotificationManager
) -> str:
    """
    Send a Twilio alert (e.g. WhatsApp/SMS) for the given flight deal.

    This is a thin wrapper around ``notifier.send_notification`` to keep
    the main loop more readable: it takes an already computed best deal and
    delegates the actual sending logic to the NotificationManager.

    :param best_deal_content: The flight deal to be advertised in the alert message.
    :param notifier: Configured NotificationManager instance used to talk to Twilio.
    :return: The Twilio message SID returned by ``notifier.send_notification``.
    """

    message_sid = notifier.send_notification(content=best_deal_content)
    return message_sid

def send_emails_to_users(
        best_deal_content: FlightData,
        data_manager: DataManager,
        notifier: NotificationManager) -> None:
    """
    Fetch all subscribed customer email addresses and email them the given flight deal.

    This helper coordinates two responsibilities:
      * Uses ``data_manager`` to read the users sheet from Google Sheets
        and build the list of customer email addresses.
      * Delegates to ``notifier`` to send one email per address, using the
        details stored in ``best_deal_content`` (price, route, dates, stops).

    :param best_deal_content: The flight deal that should be advertised to customers.
    :param data_manager: Configured DataManager instance used to access the users sheet.
    :param notifier: Configured NotificationManager instance used to send the emails.
    :return: None. Emails are sent as a side effect.
    """

    user_emails = data_manager.get_customer_emails()

    notifier.send_emails(content=best_deal_content, user_emails=user_emails)



def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notifier = NotificationManager()

    # Get the row from the table on Google Sheet
    try:
        rows, _ = data_manager.get_table(url=SHEETY_PRICES_GET)
    except ValueError as error:
        print(f"Fatal {error}")
        return

    # For each row check if there is any field empty to fill.
    for row in rows:
        # Try to check on Amadeus, gathering the ValueError in each method and print it
        try:
            # First check if an Iata Code is present for the row
            ensure_iata_code(row, flight_search, data_manager)

            # Find best deal first
            best_deal = flight_search.find_deals(
                origin_code=DEPARTURE_CITY_CODE,
                destination_code=row["iataCode"],
                max_price=float(row["lowestPrice"]),
            )

            # Send an alert with the best deal
            message_id = send_alert_if_deal(
                best_deal_content=best_deal,
                notifier=notifier,
            )

            print(f"Alert sent for {row['city']} - Twilio SID: {message_id}")

            # Send alert through email to all the emails in the users list
            send_emails_to_users(best_deal_content=best_deal,
                                 notifier=notifier,
                                 data_manager=data_manager)

        except ValueError as error_message:
            # The ValueError in each step of any method will be printed and will skip this destination
            print(f"Skipping destination: {error_message}")
            continue

if __name__ == "__main__":
    main()