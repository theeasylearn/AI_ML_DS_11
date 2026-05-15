from datetime import datetime as dt 


#convert string date into date object
birthdate = input("Enter birth date (dd/mm/YYYY)")
date1 = dt.strptime(birthdate,'%d/%m/%Y')
print(date1)

#display date object in another format (american format)
print("Date in US format",dt.strftime(date1,'%m/%d/%Y'))

#display date object in another format (indian format)
print("Date in indian format",dt.strftime(date1,'%d/%m/%Y'))

print("Good bye.")
