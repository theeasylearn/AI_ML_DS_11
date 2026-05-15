#write a program to calcualte & display simple interest 
#input is always string
amount = input("Enter amount")
rate = input("Enter rate")
year = input("Enter year")
#convert 
amount = int(amount)
rate = float(rate)
year = int(year)

#process 
si = amount * rate * year / 100
print("Simple interest =",si)
