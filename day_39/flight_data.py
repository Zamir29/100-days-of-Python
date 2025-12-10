class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self,
                 price: float,
                 departure_code: str,
                 arrival_code: str,
                 departure_date: str,
                 start_date: str,
                 end_date:str):
        self.price = price
        self.departure_code = departure_code
        self.arrival_code = arrival_code
        self.departure_date = departure_date
        self.start_date = start_date
        self.end_date = end_date