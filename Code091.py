# naver/bolg api 사용예제


import os
import sys
import urllib.request
client_id = "클라이언트 ID 값"  # 클라이언트 ID 값
client_secret = "클라이언트 PWD 값"    # 클라이언트 PWD 값
encText = urllib.parse.quote("파스타")
print(encText)
# uri는 사용할 api의 url을 입력
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
#  url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
# 파라미터로 제공한 rul에서 얻은 데이터를 반환
rescode = response.getcode()
# getcode() response의 HTTP status code를 반환
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode) 
