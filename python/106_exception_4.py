list = [True,'Star',100,25,200,'car',45,30,None,False,200]
total = 0
count = 0
for number in list:
    try:
        if isinstance(number, (int, float)) and not isinstance(number, bool):
            total += number
            count += 1
    except TypeError as error:
        print(error)
try:
    average = total / count 
except ZeroDivisionError:
    print("List has all invalid values")
else:
    print(f"total = {total} average = {average}")