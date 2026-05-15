def getSum(*numbers):
    total = 0
    # here numbers is tuple
    for num in numbers:
        #print(num)
        total = total + num
    return total 

total = getSum(100,200,1000,2500,8500)
print(total)