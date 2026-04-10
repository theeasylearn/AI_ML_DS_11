#findout maximum number from given numbers
def getSum(*numbers):
    # here numbers is tuple
    max = numbers[0]
    for index in range(1,len(numbers)):
         if numbers[index]>max:
              max = numbers[index]
    return max             
max = getSum(85,5,125,800,99)
print(max)