# if 조건문
import datetime

now = datetime.datetime.now()


# format 메소드, 매개변수 값을 {}에 넣어준다.
if now.hour < 12:
    print("지금은 {}시 이며 오전입니다".format(now.hour))

if now.hour > 12:
    print("지금은 {}시 이며 오후입니다".format(now.hour))


if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄 입니다.".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름 입니다.".format(now.month)) 

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을 입니다.".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울 입니다.".format(now.month))