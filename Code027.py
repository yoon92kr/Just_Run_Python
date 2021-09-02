#list 연결 연산자와, 요소 추가의 차이

list = [1, 2, 3]

# 연결연산자 수행 시 
output = list + list
print("원본 list : ", list)
print("연산 결과", output)

# 요소 추가 수행 시
# 자세히는 모르지만, extend로 요소 추가시 가벽이 생겨 새로운 변수로 이전 시 , 읽을 수 없게된다고 한다.
output2 = list.extend([1,2,3])
print("원본 list :", list )
print("연산 결과 :", output2)