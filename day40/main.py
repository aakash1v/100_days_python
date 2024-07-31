import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

#for row in sheet_data:
#    if row["iataCode"] == "":
#        row["iataCode"] = flight_search.get_destination_code(row["city"])
#        # slowing down requests to avoid rate limit
#        time.sleep(2)
#print(f"sheet_data:\n {sheet_data}")
#
#data_manager.destination_data = sheet_data
#data_manager.update_destination_codes()

############# Retriving data of customers... ###############
customer_email_list = []
customers_data = data_manager.get_customer_email()
# print(customer_emails)
for customer in customers_data:
    email = customer['email']
    customer_email_list.append(email)

#notification_manager.send_emails(customer_email_list, 'trial message...')
# ==================== Search for Flights and Send Notifications ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")

    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        is_direct='false')

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price} , stops: {cheapest_flight.stops}")
    # Slowing down requests to avoid rate limit
    #time.sleep(1)

    # ==================== Send Notifications and Emails  ====================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:

        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        # Send emails to everyone on the list
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)        



#        notification_manager.send_sms(
#             message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
#                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
#                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
#         )
        #notification_manager.send_whatsapp(
        #    message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        #)


