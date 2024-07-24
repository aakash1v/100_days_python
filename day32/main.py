import datetime as dt
import random
import smtplib

my_email = 'aakashkumarpy@gmail.com'
password = 'fssbfleiunrdutff'


now = dt.datetime.now()
day = now.day
month = now.month

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
with open('birthdays.csv', mode='r') as file:
    data = file.readlines()
   
birthday_dict = {}
for line in data[1:]:
    new_data = line.split(',')
    birthday_month = int(new_data[3])
    birthday_day = int(new_data[4].strip())
    birthday_dict[(birthday_month,birthday_day)] = new_data



#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if (month,day) in birthday_dict.keys():
    your_name = birthday_dict[(month,day)][0]
    your_email = birthday_dict[(month,day)][1]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
letter = random.choice(letters)
with open(f'letter_templates/{letter}', mode ='r') as file:
    data = file.read()
    new_letter = data.replace('[NAME]', your_name)
    
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr= my_email, to_addrs = your_email,
                        msg=f'Subject:Hello,{your_name}\n\n{new_letter}')
 

