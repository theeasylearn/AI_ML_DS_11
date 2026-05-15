def getResult(num1,num2):
    add = num1 + num2 
    sub = num1 - num2 
    mul = num1 * num2 
    div = num1 / num2 
    return add,sub,mul,div 
    #function returns multiple value as tuple


num1 = int(input("Enter number "))
num2 = int(input("Enter another number "))

result = getResult(num1,num2)
print(result)

# storing value into individual variable
add, sub, mul, div = getResult(num1,num2)
print(add,sub,mul,div)
add = 0
print(add)