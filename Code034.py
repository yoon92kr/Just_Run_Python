# range, for 반복문 응용

for x in range(10):
    print(str(x+1)+"번째 반복입니다.")
print()

for x in range(1, 11):
    print(str(x)+"번째 반복입니다.")
print()

for x in range(11):
    if x==0:
        x
    else:
        print(str(x)+"번째 반복입니다.")
print()

for x in range(2,5):
    print(x, "= 반복변수")
print()

for x in range(20, 9, -2):
    print(x, "= 반복 변수")
print()

#list, range, len, for 응용
list = [50,10,20,90,80,60,40,70]

for x in range(len(list)):
    print("index [",x,"] : ",list[x])
    print("index [ {} ] :  {}".format(x, list[x]))  #조금더 좋은 활용 예시