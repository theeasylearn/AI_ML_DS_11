list = [True,'Star',100,25,200,'car',45,30,None,False,200]
# list = ['Car','Bunglow','Swimming pool','Playground',False]
total = 0
count = 0
for number in list:
    try:
        # print(number,end=' ')
        if number != False and number !=True:
            total = total + number
            count = count + 1
    except TypeError as error:
        print(error)
try:
    average = total / count 
except ZeroDivisionError as error:
    print(error)
    print("List has all invalid values")
else:
    print(f"total = {total} average = {average}")