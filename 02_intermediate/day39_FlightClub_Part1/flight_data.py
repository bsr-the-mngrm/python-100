class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, fly_from, fly_to, out_date, return_date, price):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.price = price
        self.out_date = out_date
        self.return_date = return_date

    def flight_details(self):
        return f"{self.fly_from} - {self.fly_to} - {self.price} - {self.out_date} - {self.return_date}"
