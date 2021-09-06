#에러 별 예외처리
# 마지막에 에러의 상위클래스인 Exception을 통해 개발자가 예상하지 못한 exception을 대처해주는것이 바람직하다

list_number = [52,65,32,98,25]

try:
    number_input_a = int(input("값 입력 : "))
    print("{}번째 요소 : {}".format(number_input_a, list_number[number_input_a]))
    

except ValueError as exception:
    print("정수를 입력해주세요")
    print(type(exception), exception)

except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다")
    print(type(exception), exception)

except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)