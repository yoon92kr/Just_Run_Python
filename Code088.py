# 정수 표현

# 정수 N자리 표현
# :0Nd  == N자리까지 정수로 표현, 빈공간은 0
t1 = '정수 3자리 : {0:03d} , {1:03d}'.format(12345, 12)
print(t1)

# 실수 소수점 N자리 표현
# :-.Nf == 소숫점 N자리 까지 표현
t2 = "소숫점 2자리 : {0:0.2f} , 소숫점 5자리 : {0:0.5f}".format(3.123456789)
print(t2)