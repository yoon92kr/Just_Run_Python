import numpy as n

a = n.array([[2, 3], [5, 2]])
b = n.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7,], [6, 7, 2, 5, 2, ]])

print(a)
print(b)

print(b[0][0])
print(b[0][1])
print(b[0][-1])
print(b[1:, 3:])