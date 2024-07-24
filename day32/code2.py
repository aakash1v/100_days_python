import smtplib
import random
import datetime as dt

my_email = 'aakashkumarpy@gmail.com'
password = 'fssbfleiunrdutff'


now = dt.datetime.now()
weekday = now.weekday()

if weekday ==2:

    with open('quotes.txt', mode='r') as  file:
        data = file.readlines()
        quote = random.choice(data)
        print(quote)

    with smtplib.SMTP('smtp.gmail.com', port=456) as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr= my_email, to_addrs ='aakashkumarpy@gmail.com',
                            msg=f'Subject:Wednesday Motivation \n\n{quote}')


