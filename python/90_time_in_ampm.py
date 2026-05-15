#write a program to accept hours in 24 hours format from user and convert it into 12 hours format
hours = int(input("Enter hours"))
if hours>12:
    hours = hours - 12 
    msg = ' PM'
else:
    msg = ' AM'
print(f" {hours} {msg}")

