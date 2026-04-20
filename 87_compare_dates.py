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

print("good bye")


