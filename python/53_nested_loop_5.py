'''
1 3 5 7 11 13 17 19 23 29 ... 100
'''
divisor = 2

for number in range(1,101):
    isPrime = True
    while divisor<number:
        reminder = number % divisor
        if reminder==0: #
            isPrime = False
            break #loop stop (inner loop)
        divisor=divisor+1
    if isPrime == True:
        print(number,end=' ')
    divisor = 2
