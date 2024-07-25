import pandas
import smtplib
import random


my_email = 'aakashkumarpy@gmail.com'
password = 'fssbfleiunrdutff'


data = pandas.read_csv('internship_student.csv',index_col=0)
data_dict = data['Email'].to_dict()

with open('quotes.txt') as file:
    data = file.readlines()
    quote =random.choice(data)

#sending email...
for key,value in data_dict.items():
    print(value)
    print(type(value))
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user = my_email,password = password)
        connection.sendmail(from_addr = my_email, to_addrs =value,msg=
                            f"Subject:Hi, {key}\n\nA quote for u.\n\n{quote}")

