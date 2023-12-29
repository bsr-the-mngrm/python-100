class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, fly_from, fly_to, out_date, return_date, price, stop_overs=0, via_city=""):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.price = price
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city

    def message_text(self) -> str:
        if self.stop_overs == 0:
            return (f"Low price alert! Only {self.price} EUR  to fly from {self.fly_from} to {self.fly_to} "
                    f"from {self.out_date} to {self.return_date}")
        else:
            return (f"Low price alert! Only {self.price} EUR  to fly from {self.fly_from} to {self.fly_to} "
                    f"from {self.out_date} to {self.return_date}.\n"
                    f"Flight has {self.stop_overs} stop over, via {self.via_city}.")
