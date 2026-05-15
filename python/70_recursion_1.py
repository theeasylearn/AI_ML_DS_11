#define
def printNumber(number):
    if number<10:
        number = number + 1 
        printNumber(number) #recursion  number = 3
        print(number)

num = 0
printNumber(num)