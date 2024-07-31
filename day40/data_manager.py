import os
import requests
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/c5289088422f4fef879e45a4f83edc2b/flightDeals/prices' 
CUSTOMER_SHEET_ENDPOINT = 'https://api.sheety.co/c5289088422f4fef879e45a4f83edc2b/flightClubData/formResponses1'


class DataManager:

    def __init__(self):
        self._user = os.environ.get("SHEETY_USRERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_email(self):
        response = requests.get(url=CUSTOMER_SHEET_ENDPOINT)
        data = response.json()
        self.email_data = data['formResponses1']
        return self.email_data
