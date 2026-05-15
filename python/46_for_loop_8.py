#write a program to count vowels in string 
# vowels = a e i o u
#input : easylearn 
#output : 4
name = input("enter string") 
count = 0
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for letter in name:
    #print(letter)
    if letter in vowel:
        count = count + 1

print(f"vowels = {count}")