numbers = [23, 47, 85, 62, 19, 74, 56, 91, 38, 64, 27, 83, 45, 72, 68, 59, 34, 88, 21, 76]
for item in numbers:
    # print(item,end=' ')
    #item = 23 
    last = item % 10
    first = item // 10
    number = (last * 10) + first
    print(number)
