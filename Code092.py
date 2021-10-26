# naver/ 파파고 번역 api 사용예제

import os
import sys
import urllib.request
client_id = "클라이언트 ID 값" # 개발자센터에서 발급받은 Client ID 값
client_secret = "클라이언트 PWD 값" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다 네이버 번역 시스템")
data = "source=ko&target=en&text=" + encText
#source : 원본언어 언어코드 / target : 번역언어 언어코드 /  text : 번역할 문자
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)