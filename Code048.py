#함수 활용 예제

def sum_all(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
    return result

print("0~100을 모두 더한 값 : ", sum_all(0, 100))
print("0~500을 모두 더한 값 : ", sum_all(0, 500))
