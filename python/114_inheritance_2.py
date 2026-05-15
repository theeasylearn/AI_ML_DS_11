#multi level inheritance 
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
#inherit derived class
class Developer(Student):
        def code(self):
            print("I can write code in python")
        def debug(self):
            print("I can debug code in python")
            #Method Overidding
        def whatICanDo(self):
            super().whatICanDo()
            self.code()
            self.debug()

#create developer class object
d1 = Developer()
d1.whatICanDo()
d1.read() 
d1.walk()
