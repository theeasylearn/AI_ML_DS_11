import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 0, 3])

print(a)
print(b)

print("Comparing each element of 2 same sized array")
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

print(np.all(a>b))
print(np.any(a>b))