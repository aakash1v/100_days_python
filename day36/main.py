import os
import requests
from twilio.rest import Client


STOCK = "TCS"

COMPANY_NAME = "Tata Consultancy Services Ltd"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.environ.get('STOCK_API_KEY')
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(difference)

UP_DOWN = None
if difference > 0:
    UP_DOWN = '🔺'
else:
    UP_DOWN = '🔻'

diff_percent = round((difference / float(yesterday_closing_price))*100, 2)
print(diff_percent)


news_params = {
    'qInTitle': COMPANY_NAME,
    'apikey': os.environ.get('NEWS_API_KEY')
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
articles = news_response.json()['articles']

three_articles = articles[:3]


account_sid = 'AC10491fd03c7c3522911f912467b4448d'
client = Client(account_sid, os.environ.get('AUTH_TOKEN'))


formatted_articles = [f"{STOCK}: {UP_DOWN} {diff_percent}\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+12085515717',
        to='+919310322381')


