# raise 
# 강제로 예외를 발생, 일반적으로 이후 예외처리문을 만들기 전 선언하나, 사용하지 않고 
# 처리문을 완성하는것이 바람직하다

number = input("정수 입력 : ")
number = int(number)

if number > 0:
    raise NotImplementedError

else:
    raise NotImplementedError