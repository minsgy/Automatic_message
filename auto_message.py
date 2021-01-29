from twilio.rest import Client
import json

# Secret.json 읽기
with open('secretkey.json') as token:
    json_data = json.loads(token.read())
    TWILIO_TOKEN = json_data["auth_token"] # 토큰 값 가져와서 저장
    MY_PHONE_NUMBER = json_data["my_phone_number"] # 보내는 전화번호 저장(내전번)


account_sid = "ACaeb34f5e2a71994af23aef0df7801142"
auth_token  = TWILIO_TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=MY_PHONE_NUMBER, 
    from_="+15402745827",
    body="보내는 문자내용"
)

print(message.sid)