class FlightData:
    def __init__(self,price,origin_airport,destination_airport, departure_date,return_date):
        self.price=price,
        self.origin_airport=origin_airport,
        self.destination_airport=destination_airport,
        self.departure_date=departure_date,
        self.return_date=return_date
    def find_cheapest_flight(data):
        if data is None or not data['data']:
            print("No flight data found")
            return FlightData(None,None,None,None,None)
        return 1
