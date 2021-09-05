# return 키워드

def returnTest():
    print("return 키워드가 호출되었습니다.")
    return 10
    print("return 키워드 다음 코드입니다")

a = returnTest()
print(a)



def returnTest2():
    return 100

b = returnTest2()
print(b)




def returnTest3():
    return

#return 뒤에 명시된 값이 없다면 null값을 돌려준다   #오류발생 하지않음.
c = returnTest3()
print(c)