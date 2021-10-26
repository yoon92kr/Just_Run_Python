
import os
import sys
import urllib.request
import datetime
import time
import json
from configparser import *






def get_request_url(url):

    client_id = "ZXTKnpCVJT4vlpwCTXdk"  # 클라이언트 ID 값
    client_secret = "dYeIl47f7y"    # 클라이언트 PWD 값

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None

#[Code 2]
def getNaverSearchResult(sNode, search_text, page_start, display):

    base = "https://openapi.naver.com/v1/search/"
    node = "%s.json?query=%s&start=%s&display=%s" %(sNode, urllib.parse.quote(search_text), page_start, display)
    url = base + node

    retDate = get_request_url(url)

    if (retDate == None):
        return None
    else:
        return json.loads(retDate)
    
#[Code 3]
def getPostDate(post, jsonResult):

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title':title, 'description':description, 'org_link':org_link, 'link':link, 'pDate':pDate})

    return

def main():

    jsonResult = []
    sNode = 'news'
    search_text = '파스타'
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    while ((jsonSearch != None) and (jsonSearch['display'] != 0)):
        for post in jsonSearch['items']:
            getPostDate(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open ('%s_naver_%s.json' %(search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    
    print ('%s_naver_%s.json Saved!' %(search_text, sNode))

if __name__ == '__main__':
    main()


