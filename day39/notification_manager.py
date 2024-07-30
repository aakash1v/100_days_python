import os
from twilio.rest import Client

account_sid = 'AC10491fd03c7c3522911f912467b4448d'
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

#message = client.messages.create(
#  from_='+12085515717',
#  to='+919310322381'
#)

#print(message.sid)


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = client


    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_='+12085515717',
            body=message_body,
            to='+919310322381'
        )
        # Prints if successfully sent.
        print(message.sid)
   
    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_='whatsapp:+12085515717',
            body=message_body,
            to='whatsapp:+919310322381'
        )
        print(message.sid)


