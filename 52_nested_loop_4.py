'''
2) Write a program to print all divisors of numbers from 10 to 20
------------------------------------------------------------------
    10: 1, 2, 5, 10 //10/1 10/2  10/3
    11: 1, 11
    12: 1, 2, 3, 4, 6, 12
    13: 1, 13
    14: 1, 2, 7, 14
    15: 1, 3, 5, 15
    16: 1, 2, 4, 8, 16
    17: 1, 17
    18: 1, 2, 3, 6, 9, 18
    19: 1, 19
    20: 1, 2, 4, 5, 10, 20
'''
number = 10 
divisor = 1

for number in range(10,21):
    while divisor<=number:
        reminder = number % divisor
        if reminder==0: #
            print(divisor,end='  ')
        divisor=divisor+1
    print("")
    number = number + 1
    divisor = 1


