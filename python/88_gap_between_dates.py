#findout which is older date
#write a program to findout elder brother from two brother birth date given as string
from datetime import date 
def acceptDate(msg):
    print(msg)
    day = int(input("Enter day"))
    month = int(input("Enter month"))
    year = int(input("Enter year"))
    #convert date 
    birthday = date(year,month,day)
    return birthday

birthday_1 = acceptDate("enter 1st brother's birth date (day, month and year as different input)")

birthday_2 = acceptDate("enter 2nd brother's birth date (day, month and year as different input)")

if birthday_1<birthday_2:
    print("1st brother is elder brother")
else:
    print("2nd brother is elder brother")

gap = abs(birthday_1 - birthday_2)

print(gap)            # gives difference in days
print(gap.days)       # number of days
print(f"{gap.days/365:.2f}")       # number of years

