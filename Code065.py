# 예외처리_조건문 사용

user_input_a = input("정수를 입력해주세요 : ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름 : {}".format(number_input_a))
    print("원의 둘레 : {}".format(2*3.14*number_input_a))
    print("원의 넓이 : {}".format(3.14*number_input_a*number_input_a))
else:
    print("문자가 아닌 정수를 입력해 주세요")

    
