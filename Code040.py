# break 키워드
# break 키워드를 만나면, 가장 가까운 반복문을 탈출한다

count = 0

while True:
    print("{}번째 반복문 입니다".format(count))
    count += 1
    typing = input("진행을 계속 하시겠습니까? [y/n] ")
    if typing in ["y", "Y"]:
        print("반복문이 종료되었습니다")
        break
    
# python 에서의 메소드 범위는 들여쓰기로 대채한다.