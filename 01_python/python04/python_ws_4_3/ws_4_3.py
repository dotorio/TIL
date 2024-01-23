import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로

API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
dummy_data = []
for x in range(1, 11):
    response = requests.get(API_URL + str(x))
# JSON -> dict 데이터 변환
    parsed_data = response.json()
    if float(parsed_data['address']['geo']['lat']) < 80 and float(parsed_data['address']['geo']['lng']) > -80:
        new_dict = {}
        new_dict['company'] = parsed_data['company']['name']
        new_dict['lat'] = parsed_data['address']['geo']['lat']
        new_dict['lng'] = parsed_data['address']['geo']['lng']
        new_dict['name'] = parsed_data['name']
        dummy_data.append(new_dict)
print(dummy_data)