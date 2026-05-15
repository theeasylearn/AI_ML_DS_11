balance = 20000
def addMoney(amount):
    global balance 
    # balance = 0
    balance = balance + amount 

print(balance)
addMoney(99)
print("After update balanace is",balance)