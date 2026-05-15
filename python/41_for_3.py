#write  a program to display only even numbers from tuple #also count even number
numbers = (12, 45, 78, 23, 56, 91, 34, 67, 89, 10, 54, 32, 76, 88, 21, 43, 65, 99, 27, 58)
count = 0
for item in numbers:
    # print(item,end=' ')
    reminder = item % 2 #
    if reminder == 0:
        print(item,end=' ')
        count+=1 #count = count + 1
print("no of even values = ",count)