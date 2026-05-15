import math

number = float(input("Enter any one float number"))

print(f"ceil value of {number} = ",math.ceil(number))
print(f"floor value of {number} = ",math.floor(number))
print(f"truncated value of {number} = ",math.trunc(number))
print(f"absolute value of {number} = ",math.fabs(number))
print(f"fractional and integer part of {number} = ",math.modf(number))

print(f" factorial of 5 ",math.factorial(5))
print(f" copysign of 1 using -1 ",math.copysign(5,1))

