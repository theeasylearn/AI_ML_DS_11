#write a program to count vowels in string 
# vowels = a e i o u
#input : easylearn 
#output : 4
name = input("enter string") 
count = 0
for letter in name:
    #print(letter)
    if letter == 'a' or letter =='e' or letter=='o' or letter=='i' or letter == 'u' or letter == 'A' or letter =='E' or letter=='O' or letter=='I' or letter == 'U':
        count = count + 1

print(f"vowels = {count}")