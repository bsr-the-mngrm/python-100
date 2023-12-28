class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, fly_from, fly_to, out_date, return_date, price):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.price = price
        self.out_date = out_date
        self.return_date = return_date

    def sms_message(self) -> str:
        return (f"Low price alert! Only {self.price} EUR  to fly from {self.fly_from} to {self.fly_to} "
                f"from {self.out_date} to {self.return_date}")
