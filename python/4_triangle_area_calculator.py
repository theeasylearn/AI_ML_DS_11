#write a program to calculate area of triangle from given base & height 
#input
base = input("Enter base")
height = input("Enter height")

#convert
base = int(base)
height = int(height)

#process
area = 0.5 * base * height
#output
print("area of triangle =",area)