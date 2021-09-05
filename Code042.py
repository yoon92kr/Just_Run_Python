# 메소드 정의
# def 키워드를 통해 메소드를 선언한다.
# 선언 형식 def <메소드명>(매개변수): 처리문

def hello():
    print("hello")
    print("python")
    print("world")

hello()


def printRepeat(value, count):
    for i in range(count):
        print(value)



printRepeat("hello python", 5)  
# printRepeat("hello?")   #매개변수를 정의한 개수로 입력하지 않을경우 오류가 발생한다.