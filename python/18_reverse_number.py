# write a program to reverse 2 digit amount
# input : number 15 output number 51 
# input : number 95 output number 59

amount = int(input("Enter amount"))

first = amount // 10 #1
last = amount % 10 # 5 

amount = last * 10  + first 
print(amount)
