#기본 매개변수 활용 함수 예제

def sumTest(start = 0, end = 100, step = 1):
    result = 0
    for i in range(start, end+1, step):
        result += i
    return result


print("sumTest 기본 매개변수 사용 : ", sumTest())
print("sumTest 매개변수 값 지정(0,100,10):", sumTest(0,100,10))
print("sumTest 특정 매개변수 값 지정(step=5) :", sumTest(step=5))
