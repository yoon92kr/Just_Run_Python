# 기본 매개변수(초기화가 완료 된 변수)는 일반 매개변수 앞에 올 수 없다

#def testmethod(a=1, b):    #에러발생
def testmethod(a, b=1):
    print(a, b)

testmethod(2)