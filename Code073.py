# random 표준모듈
import random
#from random import random, uniform, expovariate, randrange
a = random.random()
print(int(a*100))

print(random.random()) #0이상 1.0미만 랜덤값을 반환

print(random.uniform(2.5, 10.0))    #a이상 b미만 랜덤값을 반환

print(random.expovariate(1/5))  

print(random.randrange(10)) #range와 동일한 범위 내 random

print(random.randrange(0, 101, 2))