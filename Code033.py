# range

#range(A) 0부터 A최종값 미만을 포함
print(range(5), list(range(5)))
print()

#range(A,B) A 초기값 이상, B 최종값 미만을 포함
print(range(3,6), list(range(3,6)))
print()

#Range(A,B,C) A초기값 이상, B 최종값 미만 C의 간격을 포함(음수 지원)
print(range(1,16,2), list(range(1,16,2)))
print(range(20,0,-2), list(range(20,0,-2)))