#write a program to findout median value from all the argument passed in function
def getMedian(*numbers):
    #convert tuple into list 
    numbers2 = list(numbers)
    #sort list in ascending order
    numbers2.sort()
    print(numbers2)
    size = len(numbers2)
    # print(size)
    # 15 20 25 30 40 50
    median = None
    mid = size // 2
    if size%2==0: #even 
        #55 = 30 + 25
        median = numbers2[mid] + numbers2[mid - 1]
        median = median / 2
    else:
        median = numbers[mid] 
    return median

median = getMedian(15,50,25,30,40,20)
print(median)

median = getMedian(15,50,25,30,40)
print(median)
