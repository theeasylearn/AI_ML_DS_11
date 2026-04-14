# example of lambda function 
# def getArea(length,width):
#     area = length * width 
#     return area 
# OR
getArea = lambda length,width: length * width
getPower = lambda base,exponent: base ** exponent 
getInterest = lambda amount,rate,year : (amount * rate * year) / 100

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = getArea(length, width)
print("Area:", area)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
power = getPower(base, exponent)
print("Power:", power)

amount= int(input("Enter amount: "))
rate = float(input("Enter rate: "))
year = int(input("Enter year: "))
print(" simple interest:", getInterest(amount, rate, year))

