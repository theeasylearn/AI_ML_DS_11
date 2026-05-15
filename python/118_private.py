class Account:
    def __init__(self,name,balance):
        self.name = name 
        #create private variable
        self.__balance = balance
    def updateBalance(self,amount):
        self.__balance = self.__balance + amount 
    def display(self):
        print("Balance ",self.__balance)

a1 = Account(name='Ram Patel',balance = 25000000)
a1.display()
a1.updateBalance(99)
a1.display()
a1.updateBalance(-150)
a1.display()
# it should not be possible 
a1.__balance =  9999999999
a1.display()
