from datetime import datetime as dt 
from datetime import timedelta 

#accept date from user 
date1 = input("enter date (%d/%m/%Y )")

#convert it into actual date object
date1 = dt.strptime(date1,'%d/%m/%Y')

print(date1)
no_of_days = int(input("Enter how many days you want to add in date"))

#add days into date
delta = timedelta(days=no_of_days)

#add difference into date 
new_date = date1.__add__(delta)
print(new_date)