#factorial 재귀함수
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))



def factorial2(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial2(n-1)

print("1!:", factorial2(1))
print("2!:", factorial2(2))
print("3!:", factorial2(3))
print("4!:", factorial2(4))
print("5!:", factorial2(5))