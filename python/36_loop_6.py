# 1 -2 3 -4 5 -6 7 -8 .... 1000

number = 1
while number<1000:
    reminder = number % 2 #1
    if reminder == 1:
        print(number)
    else:
        print(0-number)
    number = number + 1 #2 

