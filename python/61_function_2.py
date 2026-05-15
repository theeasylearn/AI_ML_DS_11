#write a program that return maximum number from two number  
def getMax(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2 

num1 = int(input("Enter number"))
num2 = int(input("Enter another number"))

print(num1,num2)
#function call
max = getMax(num1,num2)
print(max)