# in 키워드
array = [15, 35, 60, "apple", "orange"]

print(array)
print("15 in array : ", 15 in array)
print("40 in array : ", 40 in array)
print("60 in array : ", 60 in array)
print("apple in array : ", "apple" in array)
print("banana in array : ", "banana" in array)


i=0
for x in array:

    print("index [",i,"] : ", x)
    i += 1
