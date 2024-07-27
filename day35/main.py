import os
import requests

from twilio.rest import Client

account_sid = 'AC10491fd03c7c3522911f912467b4448d'
client = Client(account_sid, os.environ.get('AUTH_TOKEN'))


OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
        'appid': os.environ.get('OWM_API_KEY'),
        'lat': 22.5744,
        'lon': 88.3629,
        'cnt': 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)

weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']

    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+12085515717',
        to='+919310322381')

print(message.status)


