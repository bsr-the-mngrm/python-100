class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_id, fly_from, fly_to, date_from, date_to, price):
        self.id = flight_id
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.price = price
        self.date_from = date_from
        self.date_to = date_to
