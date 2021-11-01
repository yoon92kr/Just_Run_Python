import json


with open('서울특별시_관광지입장정보_2020_2021.json', encoding="utf8") as json_file:
    # open 메소드의 default type은 'r'이다.
    yoon = json.load(json_file)

print(yoon)