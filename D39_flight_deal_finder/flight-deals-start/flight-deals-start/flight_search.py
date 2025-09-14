import requests
from data_manager import *

AMADEUS_HOST_URL="https://test.api.amadeus.com/v1"
AMADEUS_API_KEY="VCnYGeJ4U69FpAoFoOWdpxDkOGzjB8NE"
AMADEUS_ACCESS_TOKEN="mxIaE7jchqAnG0pktbzadL99HcAK"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flights = []
        self.search_iata_code()

    def search_iata_code(self):
        headers={"Authorization":"Bearer "+AMADEUS_ACCESS_TOKEN}
        data_manager = DataManager()
        sheety_data=data_manager.table_data
        for row in sheety_data :
            parameters={
                "keyword":row["city"].upper(),
            }

            res=requests.get(AMADEUS_HOST_URL+"/reference-data/locations/cities",params=parameters,headers=headers)
            # city_data=res.json()["data"]
            print(res)
            # write IATA code into sheety

            # if city_data["data"]:

