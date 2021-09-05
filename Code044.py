# 기본 매개변수
# 매개변수를 입력하지 않을 경우, 기본으로 대입 될 값을 설정

def printTest(value, count =2):
    for counts in range(count):
        print(value)



printTest("hello")  #count 값의 인자를 지정해주지 않는다면, 설정값이 대입된다
print()
printTest("안녕", 5)    #count 값을 지정하게되면 기본값 대신 대입되게 된다.
