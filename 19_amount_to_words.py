#write a program to display 2 digit amount into words 
#input 45 output four five 
#input 96 output nine six  
#input 17 output one seven 

amount = int(input("Enter 2 digit amount"))
words = ['zero','one','two','three','four','five','six','seven','eight','nine']

first = amount // 10 #four
last = amount % 10 #five
print(first,last)
print(words[first]," ",words[last])