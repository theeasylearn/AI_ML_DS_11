#write a program to print multiplication table of 1 to 10 
#  1 x 1 = 1
#  1 x 2 = 2
#  1 x 10 = 10

#  2 x 1 =   2
#  2 x 2 =   4
#  2 x 10 = 20

number = 1

while number<=10:  #outer loop 
    multiplier = 1
    while multiplier<=10: #inner loop
        result = number * multiplier
        print(f"{number} X {multiplier} = {result}")
        multiplier = multiplier + 1
    number = number + 1

