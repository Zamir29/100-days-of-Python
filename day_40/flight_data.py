class FlightData:
    """Represents a single best flight deal returned by the search layer.

    This class is used as a small value object that travels between
    `FlightSearch` and `NotificationManager`, so the rest of the app
    doesn't need to know about the raw Amadeus JSON structure.

    Attributes:
        price (float): Total ticket price in the provider's currency.
        departure_code (str): IATA code of the departure city/airport
            (e.g. 'MIL').
        arrival_code (str): IATA code of the arrival city/airport
            (e.g. 'BCN').
        departure_date (str): Date of the flight in 'YYYY-MM-DD' format.
        start_date (str): Start of the search window used to query Amadeus,
            in 'YYYY-MM-DD' format.
        end_date (str): End of the search window used to query Amadeus,
            in 'YYYY-MM-DD' format.
    """
    #This class is responsible for structuring the flight data.

    def __init__(self,
                 price: float,
                 departure_code: str,
                 arrival_code: str,
                 departure_date: str,
                 start_date: str,
                 end_date:str,
                 stops:int):
        self.price = price
        self.departure_code = departure_code
        self.arrival_code = arrival_code
        self.departure_date = departure_date
        self.stops = stops
        self.start_date = start_date
        self.end_date = end_date