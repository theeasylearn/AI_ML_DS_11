class Animal:
    def run(self):
        print("I can run")
    def hunt(self):
        print("I can hunt")

class Bird:
    def fly(self):
        print("I can fly")
    def chippering(self):
        print("I can do chippering")

class Dragon(Animal,Bird):
    def fire(self):
        print("I can throw fire from mouth")
    def whatICanDo(self):
        super().run()
        super().hunt()
        super().fly()
        super().chippering()

d1 = Dragon()
d1.whatICanDo()
