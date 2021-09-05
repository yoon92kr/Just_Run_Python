
# countinue 키워드
# 해당 키워드를 마주하면, 이후 처리문을 무시한 뒤 조건문으로 회귀한다.
list = [1,52,7,2,64,77]

for num in list:
    if num < 10:
        continue
    print(num)      
#해당 print메소드는 for문에 종속한다, 만일 if문에 종속되어 처리할 경우 else에 print를 입력해야한다.

