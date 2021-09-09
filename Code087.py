# 문자열 정렬

# :>10 == 해당 format을 10의 공간 중 우측정렬을 한다
t1 = 'this is {0:>10}  | done {1:>5}|'.format('right', 'a')
print(t1)

t2 = 'this is {0:<10}  | done {1:<5}|'.format('left', 'a')
print(t2)

t3 = 'this is {0:^10}  | done {1:^5}|'.format('center', 'a')
print(t3)

# :>10 == 해당 format을 10의 공간을 _로 채우고 자료값은 우측정렬을 한다
t4 = 'this is {0:_>10}  | done {1:_>5}|'.format('right', 'a')
print(t4)

t5 = 'this is {0:.<10}  | done {1:.<5}|'.format('left', 'a')
print(t5)

t6 = 'this is {0:x^10}  | done {1:x^5}|'.format('center', 'a')
print(t6)