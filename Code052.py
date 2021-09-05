# 튜플 tuple
# 튜플은 초기화가 끝난 뒤 값대입이 불가능하다

tuple_test = (1,2,3)

print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])

#tuple_test[0] = 10

[a, b] = [10, 20]
(c, d) = (10, 20)

print("a :",a)
print("b :",b)
print("c :",c)
print("d :",d)

# 괄호를 사용하지 않아도 자동으로 tuple화 된다.
tuple_test_2 = 10, 20, 30 ,40
print(tuple_test_2)
print(type(tuple_test_2))

a, b, c = 10, 20, 30
print(a, type(a))
print(b, type(b))
print(c, type(c))

z,y = 10,20,30,40
print(z)
print(y)