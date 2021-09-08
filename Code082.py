import urllib3
from bs4 import BeautifulSoup

def get_html_from_naver_search(keyworld):
    burl = 'https://search.naver.com/search.naver?query='
    surl = burl + keyworld
    req = urllib3.PoolManager()
    return req.request('GET', surl).data
    

result = get_html_from_naver_search('파이썬')
parsed = BeautifulSoup(result,'html.parser')

print("surl의 title 태그를 찾아 반환 : ", parsed.title)

print("surl의 p 태그를 찾아 반환 : ", parsed.p)

print("surl의 a 태그를 찾아 반환 : ", parsed.find('a'))