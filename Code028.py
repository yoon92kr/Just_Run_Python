# 리스트 메소드 _ 요소 제거
list = [0,1,2,3,4,5,6]
print("list : ", list)
print()

#del 예약어는 해당 index 혹은 index 범위를 제거한다.
del list[0]
print("del list[0]: ", list)

del list[2:4]
print("del list[2:4]: ", list)
print()

#pop 메소드는 값을 반환 후 제거한다.
print("list.pop(0): ", list.pop(0))
print("list : ",list)