#while 반복문 활용

list = [1,2,1,2]
value = 2

# list의 순차적으로 value 와 같은 값이 있는지 여부를 확인 후 처리문으로 진행된다고 생각하면 된다..
# 더 공부할것
while value in list:
    list.remove(value)

print(list)


for value in list:
    list.remove(value)

print(list)