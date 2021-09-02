# list []
# 모든 자료형이 혼용될 수 있다.
# list변수를 print문에 넣을경우, list type인것을 표기해준다 "[ ]"
array = [1, 2, 3, "문자열", True, False]
print(array)

print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])
print(array[5])

# index에 새로운 값을 대입할 경우, 치환된다.
array[0] = "새로운 값 대입"
print(array)
print(array[0])

# python 에서는 역인데스를 사용할 수 있다.
print(array[-1])
print(array[-2])
print(array[-3])