#single level inheritance 
#create parent class
class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")

#create child class 
class Student(Person):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        print("Now whatCanDo method start....")
        super().walk()
        super().talk()
        super().eat()
        self.read()
        self.write()
        print("whatCanDo method finish....")

#create person class object
p1 = Person()
p1.walk()
p1.talk()
p1.eat()


#create child class object
s1 = Student()
s1.whatICanDo()
s1.walk() #calling parent class method using child class object is possible 
s1.read()
