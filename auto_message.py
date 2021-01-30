from twilio.rest import Client
import csv
import json

# 휴대폰 번호 저장 하기
number_array = []

# Secret.json 읽기
with open('secretkey.json') as token:
    json_data = json.loads(token.read())
    TWILIO_TOKEN = json_data["auth_token"] # 토큰 값 가져와서 저장
    MY_PHONE_NUMBER = json_data["my_phone_number"] # 보내는 전화번호 저장(내전번)


# CSV 데이터열기

data_file = open('test.csv', 'r', encoding='utf-8')
reader = csv.reader(data_file)
for line in reader:
    if len(line[4]) > 12:
        temp = line[4].split('-')
        number_array.append(''.join(temp))
    else:
        number_array.append(line[4])

# 전송 연락처 명단
for number in number_array:
    print(number)
        
# 파일 닫기
data_file.close()

# 문자 API id + token
account_sid = "AC7e395a1420bb05fded85b3d46a896b57"
auth_token  = TWILIO_TOKEN

client = Client(account_sid, auth_token)

# for number in number_array:
#     message = client.messages.create(
#         to='+82'+number, 
#         from_=MY_PHONE_NUMBER,
#        body="밈미/두부 제껍니다 -괴도키드-"
#     )

# print(message.sid)