# 가변 매개변수와 기본 매개변수를 같이 사용
# 가변매개

def printTest(n=2, *value):
    for i in range(n):
        for v in value:
            print(v, end="")
        print()


printTest("hello", "funny", "python")

#기본 매개변수를 맨 뒤에 둘 경우, 해당 매개변수 명을 같이 기입해주어야한다
#어디까지가 가변 매개변수의 인자값인지 알 수 없기 때문이다.

def printTest2(*value, n=2):
    for i in range(n):
        for v in value:
            print(v, end="")
        print()

printTest2("hello", "funny", "java", n=3)
# 매개변수 키워드를 직접 명시해 줄 경우에는 순서는 문제되지 않는다.