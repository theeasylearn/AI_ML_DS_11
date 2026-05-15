class MyTime:
    #constructor
    def __init__(self,hour,minutes,seconds):
        self.hour = hour #3  
        self.minutes = minutes # 10 
        self.seconds = seconds #7
        print("constructor called...")
    def toSeconds(self):
        totalSeconds = self.hour * 60 * 60
        totalSeconds = totalSeconds + (self.minutes * 60)
        totalSeconds = totalSeconds + self.seconds
        return totalSeconds
    
    #develop function toMinutes that return minutes 

hours = int(input("Enter hours"))
minutes = int(input("Enter minutes"))
seconds = int(input("Enter seconds"))

#object = className 
m1 = MyTime(hours,minutes,seconds) #constructor function executes 
totalSeconds = m1.toSeconds()
print(f"total seconds = {totalSeconds}")

