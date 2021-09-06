# try - except , else 사용
# try 구문 내에 오류발생이 확실한 코드만 선언
# finally 구문은 필수요건이 아니나, 선언 시 반드시 실행된다
try:
     number_input_a = int(input("정수를 입력해주세요 : "))
    
#except:
#    print("문자가 아닌 정수를 입력해 주세요")

except Exception as exception:
    print("type(exception) : ", type(exception))
    print("exception : ", exception)

else:
    print("원의 반지름 : {}".format(number_input_a))
    print("원의 둘레 : {}".format(2*3.14*number_input_a))
    print("원의 넓이 : {}".format(3.14*number_input_a*number_input_a))

finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")    
