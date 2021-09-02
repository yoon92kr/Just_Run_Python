#복잡한 코드

number = input("정수를 입력해주세요")

#number = int(number)

#number = str(number)


last_number = number[-1]
last_number = int(last_number)

if last_number == 0 or  last_number == 2 or last_number == 4 or last_number ==6 or last_number ==8:
    print("짝수입니다")

if last_number == 1 or last_number == 3 or last_number == 5 or last_number == 7 or last_number == 9:
    print("홀수입니다")


    