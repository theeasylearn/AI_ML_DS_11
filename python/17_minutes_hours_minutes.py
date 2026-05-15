# write a program to figure out hours and remaining minutes from given minutes 
# input : minutes 195 output : hours 3 and minutes 15
# input : minutes 79 output : hours 1 and minutes 19
# input : minutes 49 output : hours 0 and minutes 49

minutes = int(input("Enter given minutes"))

#minutes = 75
#calculate  hours 
hours = minutes // 60
minutes = minutes % 60 

print("hours =",hours, " minutes =",minutes)
