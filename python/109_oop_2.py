class Person:
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")

#we must create object
ram = Person()
ram.eat()
ram.sleep()
ram.talk()
ram.walk()

#create another object 
mohan = Person()
mohan.talk()
mohan.eat()
mohan.sleep()
mohan.walk()

