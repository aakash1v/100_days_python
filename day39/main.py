#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import time

api_secret = '2ZTGONw6cYwT66BO'
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
api_key = 'Y3Gpit1HXyPQgr15X2N1e0bosRrfD9WT'


# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"
notification_manager = NotificationManager()

#now = datetime.datetime.now()
#today = now.strftime('%Y-%m-%d')
#
#sheet_data = DataManager()

#print(sheet_data.get_data())

#data = {
#    'price': {
#        'city': 'Patna',
#        'iataCode': '',
#        'lowestPrice': 120
#    }
#}

# print(sheet_data.post_data(data))

# for i in range(2, 12):
#     print(sheet_data.update_data(i, updated_data))

#print(sheet_data.delete_row(12))

#fs = FlightSearch()
#print(fs._token)
#print(fs.get_destination_code('london'))

# updating iataCode of cities...
#data_list = sheet_data.get_data()

#cities =[]
#for data in data_list:
#    for key, value in data.items():
#        if key == 'city':
#            cities.append(value)


#i = 1 
#for city in cities:
#    i += 1
#    iata_code = fs.get_destination_code(city)
#    updated_data = {
#        'price': {
#            'iataCode': iata_code
#        }
#    }
#    sheet_data.update_data(i, updated_data)
"""
destination_locations = []
data_list = sheet_data.get_data()
for data in data_list:
    destination_locations.append(data['iataCode'])


#print(destination_locations)


headers = {"Authorization": f"Bearer {fs._token}"}
query = {
    'originLocationCode': 'LON',
    'destinationLocationCode': 'TYO',
    'departureDate': '2024-07-31',
    'adults': 1
}
"""

#response = requests.get(url=FLIGHT_ENDPOINT, params=query, headers=headers)
#print(response.json())

# ==================== Search for Flights ====================

# ==================== Search for Flights and Send Notifications ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:

    print(f"Getting flights for {destination['city']}")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)

    if cheapest_flight.price != "N/A" and float(cheapest_flight.price) < float(destination["lowestPrice"]):
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
             message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
         )
