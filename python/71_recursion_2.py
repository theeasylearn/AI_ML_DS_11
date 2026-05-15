#write a program to convert decimal number into binary number 
def printBinary(number):
    if number>0:
        reminder = number % 2
        number = number // 2 #48 
        printBinary(number)
        print(reminder,end='')

number = int(input("Enter number"))
printBinary(number)