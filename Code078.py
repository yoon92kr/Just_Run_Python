# 웹 크롤링
# rss 주소를 가져와 필요한 태그의 자료값만 추출
# select(A) A의 데이터를 리스트 형식으로 모두 가져옴
# select_one(A) A의 태그 중 첫번쩨 데이터만 문자열로 가져옴

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=133")
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시 : ", location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)
    print()