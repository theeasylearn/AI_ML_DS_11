from datetime import date 

print("enter your birth date (day, month and year as different input)")

day = int(input("Enter day"))
month = int(input("Enter month"))
year = int(input("Enter year"))

#convert date 
birthday = date(year,month,day)
print(birthday)
