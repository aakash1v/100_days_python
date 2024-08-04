from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
import pprint

load_dotenv()

my_email = os.getenv('EMAIL_ADDRESS')
my_password = os.getenv('EMAIL_PASSWORD')
headers = {'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

############ Getting current price of instant pot ###############

# URL = 'https://appbrewery.github.io/instant_pot/'
URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

price_element = soup.find(name='span', class_='aok-offscreen').getText()
instant_pot_price = float(price_element.split('$')[-1])
# pprint.pp(soup)
#print(instant_pot_price)

product_title = soup.find(name='span', id='productTitle').getText().strip()
#print(product_title)

############ Sending Email.. ################

BUY_PRICE = 100
message = f"{product_title} is on sale for {instant_pot_price}!"

if BUY_PRICE > instant_pot_price:

    with smtplib.SMTP(os.getenv('SMTP_ADDRESS', 587)) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs='aakashkumarpy@gmail.com',
                            msg=f'Subject:Amazon price Alert!\n\n{message}\n{URL}'.encode('utf-8'))
        


