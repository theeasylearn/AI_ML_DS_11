#write a program to count digits  given string  
line = input("Enter one line ")
print(line) #line ankit3385
count = 0 
digits = ['0','1','2','3','4','5','6','7','8','9']

for letter in line:
    # //print(letter,end=' ')
    if letter in digits:
        count=count + 1

print("No of digits ",count)