# 딕셔너리
# 키:값 으로 나뉘어지며 값에는 리스트 형식도 올 수 있다.

dicTest = {
    "name" : "Yoon",   # 키의 값은 중복을 허용하지 않으며, 값은 중복을 허용한다
    "name" : "Yoon",
    "age" : 30,
    "address" : "대전",
    "hobby" : ["java", "python", 50]
}

print("print(dicTest) : ",dicTest)
print()

#dictionaty의 키를 통해 값을 반환할 수 있다.
print('dicTest["name"] : ', dicTest["name"])
print('dicTest["hobby"] : ', dicTest["hobby"])
print()

# 키의 값을 대입연산자를 통해 변경이 가능하다
dicTest["age"]=28
print('dicTest["age"]=28')
print("print(dicTest) : ",dicTest)
print()

# 요소 추가
dicTest["weight"]=83
dicTest["height"]=183
print("dicTest 요소 추가 후 : \n",dicTest)
print()

# 요소 제거
del dicTest["address"]
del dicTest["hobby"]
print("dicTest 요소 제거 후 : \n", dicTest)
print()

# in 키워드를 통한 boolean 반환
print('"name" in dicTest :', "name" in dicTest)
print('"hobby" in dicTest :', "hobby" in dicTest)

# print(dicTest["존재하지 않는 key"])   #존재하지 않는 key를 호출할때는 에러가 발생하기 때문에 in 키워드를 통한 에러방지나 try 키워드를 사용하는것이 바람직하다
if "존재하지 않는 key" in dicTest:
    print(dicTest["존재하지 않는 키"])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")