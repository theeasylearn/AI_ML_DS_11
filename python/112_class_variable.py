class Society:
    #class variable
    hall = "ABC Community Hall"
    def __init__(self,flatno,owner):
        self.flatno = flatno 
        self.owner = owner
    def display(self):
        print("Flat No ",self.flatno)
        print("Owner = ",self.owner)
    

print("Hall ",Society.hall) # ABC Community Hall
Society.hall = 'XYZ Marriage Hall'
print("Hall ",Society.hall) # ABC Community Hall

s1 = Society(101,'Ankit Patel')
s2 = Society(102,'Jiya Patel')
s3 = Society(103,'Diya Patel')
s4 = Society(103,'Kashish Patel')

s1.display()
s2.display()
s3.display()
s4.display()

print("Hall ",s1.hall)
print("Hall ",s2.hall)
print("Hall ",s3.hall)
print("Hall ",s4.hall)