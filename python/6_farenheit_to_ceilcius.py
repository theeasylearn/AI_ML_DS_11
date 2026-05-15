# write a program to convert & display fahrenheit into celsius   
#input 
fahrenheit = input("Enter fahrenheit ")
#convert
fahrenheit = float(fahrenheit)
#process 
celsius = (fahrenheit - 32) / 1.8
celsius = round(celsius,2)
print("celsius = ",celsius)