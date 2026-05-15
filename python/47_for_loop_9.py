#write a program to count digits  given string  
line = input("Enter one line ")
print(line) #line ankit3385
count = 0 
for letter in line:
    # //print(letter,end=' ')
    if letter == '0' or letter=='1' or letter=='2' or letter=='3' or letter=='4' or letter=='5' or letter=='6' or letter == '7' or letter == '8' or letter =='9':
        count=count + 1

print("No of digits ",count)