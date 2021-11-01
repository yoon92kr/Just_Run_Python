import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = "https://media.daum.net/"

soup = bs(ur.urlopen(url).read(), 'html.parser')

print(soup.find_all('div', {"class": "item_issue"}))
# 특정 클래스 속성 출력

print(soup.find_all('a')[:5])
# a태그 5개 출력

for i in soup.find_all('a')[:5]:
    print(i.get('href'))
# 태그의 링크 5개 출력

article1 = "https://news.v.daum.net/v/20211028165607164"

soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

for i in soup2.find_all('p'):

    print(i.text)


f = open('lins.txt', 'w')

for i in soup.find_all('div', {"class": "item_issue"}):
    f.write(i.find_all('a')[0].get('href')+'\n')
    f.close

url = "https://news.daum.net/"
soup = bs(ur.urlopen(url).read(), 'html.parser')
f = open('article_total.txt', 'w')

for i in soup.find_all('div', {"class": "item_issue"}):
    try:
        f.write(i.text+'\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get(
            'href')).read(), 'html.parser')

        for j in soup2.find_all('p'):
            f.write(j.text)

    except:
        pass

f.close()
