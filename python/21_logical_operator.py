#logical operator 
a = 10 
b = 20 
c = 30

result = a < b and  b < c #True
print(f"{result} {a} < {b} and {b} < {c}")
result = a <= b and  b >= c #True
print(f"{result} {a} <= {b} and {b} >= {c}")

result = a != b and  b != c  and a < b 
print(f"{result} {a} != {b} and {b} != {c} and {a} < {b}")
