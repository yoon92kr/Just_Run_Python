# 두가지만으로 구분되지 않는 조건에 이용한다


import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("현재는 봄입니다.")
elif 6 <= now.month <= 8:
    print("현재는 여름입니다")
elif 9<= now.month <= 11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")