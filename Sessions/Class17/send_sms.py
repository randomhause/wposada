#dowload the twilio-python library from httP://twilio.com/docs/libraries
#cmd pip install twilio

from twilio.rest import TwilioRestClient

#find these values at https://twilio.com/user/account
account_sid = "" #account number
auth_token = "" 
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="xxx", from_="xxx", body="Hello there! test3")