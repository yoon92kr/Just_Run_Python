import Code094
import re
# 미리 생성해둔 csv파일 open/write/switch 모듈 호출(Code094)

apt = Code094.switch(Code094.opencsv('apt_202110.csv'))


# print(apt[:3])
# 3개의 튜플 선택 후 콘솔출력

#15억 이상의 거래내역 시군구 / 면적 / 금액 / 건축년도 반환
new_list = []
index = []
index = apt[0]
new_list.append([index[0], index[4], index[5], index[-5], index[-3]])


for i in apt:
    

    try:
        if i[-5] > 300000:

            new_list.append([i[0], i[4], i[5], i[-5], i[-3]])

    except : pass

Code094.writecsv('over150_local.csv', new_list)

    

