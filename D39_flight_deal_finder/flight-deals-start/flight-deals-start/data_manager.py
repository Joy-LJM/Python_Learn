import requests

SHEETY_HOST_URL="https://api.sheety.co/83c8b35ea80b99481e6cf6ff2d334de3/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.table_data=[]
        self.read_data()

    def read_data(self):
        res=requests.get(SHEETY_HOST_URL)
        res.raise_for_status()
        self.table_data=res.json().get("prices")