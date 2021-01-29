from twilio.rest import Client
import json

# token 값 숨기기
with open('secretkey.json') as token:
    json_data = json.loads(token.read())
    TWILIO_TOKEN = json_data["auth_token"]
    MY_PHONE_NUMBER = json_data["my_phone_number"]


account_sid = "ACaeb34f5e2a71994af23aef0df7801142"
auth_token  = TWILIO_TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=MY_PHONE_NUMBER, 
    from_="+15402745827",
    body="Hello from Python!"
)

print(message.sid)