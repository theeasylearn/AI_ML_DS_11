import numpy as np
a = np.array([10, 20, 30, 40, 50])
#mathematical operations
print(a)
print("relational operations")
print(a>25)
print(a<25)
print(a == 40)
print(a != 30)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A)
print(B)
print("Matrix multiplication")
print(A @ B)
print(np.dot(A,B))

print("Aggregate  operations")
print("sum of all values",np.sum(a))
print("mean of all values",np.mean(a))
print("minimum of all values",np.min(a))
print("maximum of all values",np.max(a))
print("median of all values",np.median(a))


