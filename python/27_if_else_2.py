#write a program to find out profit or loss amount from given products purchase and sales price 
# Input : purchase price & sale price 
#process : calculate difference betweeen purchase and sale price 
#output : profit or loss message

purchase_price = int(input("Enter purchase price")) 
sales_price = int(input("Enter sales price"))
difference = sales_price - purchase_price
# == != < > <= >=
if difference>0:
    print(f"you have made profit {difference}")
else:
    print(f"you have made loss of {difference}")

