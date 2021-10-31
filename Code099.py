import os
import sys
import urllib.request
import datetime
import time
import json
from configparser import *
import math


def get_request_url(url):

    req = urllib.request.Request(url)

    try : 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Succes" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s} Error for Url : %s" %(datetime.datetime.now(), url))
        return None

# [Code 1]
def getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems):
    access_key="zKeBsr6gCLtS7Tj384GhKwO8Z1xP50DFyFjX3KRmg6MNDcaGsx1VA0tEdRrLnSt39JSmmiu25YtRD%2BSfa85Otg%3D%3D"
    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"

    parameters = "?_type=json&serviceKey="+access_key
    parameters += "&YM="+yyyymm
    parameters += "&SIDO="+urllib.parse.quote(sido)
    parameters += "&GUNGU="+urllib.parse.quote(gungu)
    parameters += "&RES_NM=&pageNO="+str(nPagenum)
    parameters += "&numOfRows="+str(nItems)

    url = end_point + parameters

    retDate = get_request_url(url)

    if (retDate == None):
        return None
    else :
        return json.loads(retDate)

# [Code 2]
def getTourPointData(item, yyyymm, jsonResult):
    
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm']
    rnum = '' if 'rnum' not in item.keys() else item['rnum']
    ForNum = '' if 'ForNum' not in item.keys() else item['ForNum']
    NatNum = '' if 'NatNum' not in item.keys() else item['NatNum']
   
    jsonResult.append({'yyyymm' : yyyymm, 'addrCd' : addrCd, 'gungu' : gungu ,'sido' : sido, 'resNm' : resNm, 'rnum' : rnum, 'ForNum' : ForNum, 'NatNum' : NatNum})
    return

def main():

    jsonResult = []

    sido = '서울특별시'
    gungu = ''
    nPagenum = 1
    nTotal = 0
    nItems = 100

    nStartYear = 2020
    nEndYear = 2022

    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):

            yyyymm = "{0}{1:0>2}".format(str(year), str(month))

            nPagenum = 1

            # [Code 3]
            while True:
                jsonDate = getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems)

                if (jsonDate['response']['header']['resultMsg'] == 'OK'):
                    nTotal = jsonDate['response']['body']['totalCount']

                    if nTotal == 0:
                        break

                    for item in jsonDate['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)

                    nPage = math.ceil(nTotal / 100)
                    if (nPagenum == nPage):
                        break

                    nPagenum += 1

                else :
                    break
    retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    print(retJson)
    #with open('%s_관광지입장정보_%d_%d.json' %(sido, nStartYear, nEndYear -1), 'w', encoding='utf8') as outfile:
    #    retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    #    outfile.write(retJson)


    print ('%s_관광지입장정보_%d_%d.json SAVED' %(sido, nStartYear, nEndYear-1))

if __name__ == '__main__':
    main()

