# if else
# if 구문만 사용하게 됬을 경우, 조건을 충족시켜 원하는 반환값을 받아낸다 하더라도, 이후 만나는
# 모든 if구문을 시행하기 때문에 처리가 오래걸린다.

number = input("정수를 입력해주세요")
number = int(number)

if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")