# This file will need to use the DataManager, FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from notification_manager import NotificationManager
from data_manager import DataManager

if __name__ == '__main__':
    dm = DataManager()
    nm = NotificationManager()
    deals = dm.get_deals()

    origin_city = "Budapest"
    origin_city_iata = dm.flight_search.get_iata_code(origin_city)
    tomorrow = datetime.today() + timedelta(days=1)
    end_date = datetime.today() + timedelta(days=30*6)

    for deal in deals:
        cheapest_flight = dm.flight_search.get_cheapest_flight((origin_city, origin_city_iata),
                                                               deal['iataCode'], tomorrow, end_date)

        if cheapest_flight is not None:
            if cheapest_flight.price < int(deal['lowestPrice']):
                deal['lowestPrice'] = cheapest_flight.price
                dm.update_deal(deal)
                nm.send_sms(cheapest_flight)
                print(cheapest_flight.message_text())
            else:
                print(f"There is no cheaper flight between {origin_city} and {deal['city']}.")
