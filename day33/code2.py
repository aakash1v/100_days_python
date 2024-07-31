import requests
from datetime import datetime
import smtplib
import time

my_email = 'aakashkumarpy@gmail.com'
my_password = 'fssbfleiunrdutff'


MY_LAT = 36.7201600
MY_LONG = -4.4203400

def is_iss_overhead():

    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data  = response.json()

    iss_lattitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    print(iss_lattitude, iss_longitude)

    # Your position is within +5 or -5 degrees of the ISS Position
    if MY_LAT -5 <= iss_lattitude  <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5 :
            return True


def is_night():

    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }


    response = requests.get('https://api.sunrise-sunset.org/json', params =
                            parameters )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])


    time_now = datetime.now().hour

    if time_now  >= sunset or time_now <=  sunrise :
        return True

while True:
    time.sleep(60)
    
    if is_iss_overhead() and is_night():

        with smtlib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr = my_email, to_addrs = my_email,
                                msg='Subject:LOOK UP..\n\nThe ISS is above you in the SKY.')

