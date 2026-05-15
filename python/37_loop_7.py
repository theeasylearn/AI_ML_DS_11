# 1 5 14 30 55 ... 1000

number = 1
previous = 0
temp = 0
while temp<819:
    temp = number * number + previous
    print(temp)
    previous = temp # 1
    number = number + 1 #2


