import numpy as n

discount = 0.05
cashflow = 100

def presetvalue(n):
    return (cashflow / (1+discount) **n)

print(presetvalue(1))

for i in range(20):
    print(presetvalue(i))