import smtplib

my_email = 'examplenamez543@gmail.com'
password = 'btrorvywkjsqvlqx'


with smtplib.SMTP('smtp.gmail.com', port=587) as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr= my_email, to_addrs ='example_usr@yahoo.com',
                        msg='Subject:Hello\n\nThis is the body of my email.')
    


