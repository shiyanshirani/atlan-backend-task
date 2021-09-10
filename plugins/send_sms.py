import os, csv
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Outbound SMS
def send_notification(filepath, *args):
    print('Sending notifcations')
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN') 

    client = Client(account_sid, auth_token)

    with open(f'{filepath}', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                client.messages.create(
                    to=str(row[2]),
                    from_="+14243532289",
                    body="We have received your response. Thank you for being a part of our data drive."
                )
            except Exception as e:
                print(e)
 
    print('Notifications sent to customers.')