# write a program to findout & display how many days given month has 
'''
step 
1  accept month from user 
2  check this month is 2nd 
     then display this month has 28/29 days 
3  check this month is 4 or 6 or 8 10
     then display this month has 30 
    otherwise 
     then display this month has 31 days 
'''
month = int(input("Enter months"))
if month==2:
    print("this month has 28/29 days")
    exit()
if month == 4 or month == 6 or month == 8 or month == 10:
    print("this month has 30 days")
else:
    print("this month has 31 days")

print("good bye")