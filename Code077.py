# urllib 모듈
# URL을 다루는 라이브러리
# 인터넷 주소 활용 시 사용

from urllib import request

url = request.urlopen("http://www.naver.com")   #urlopen() 메소드로 메인 페이지를 읽은 뒤 대입
output = url.read()

print(output)