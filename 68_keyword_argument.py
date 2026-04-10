def getMerit(maths,science,english,gujarati,hindi,computer):
    print(f"maths = {maths} science = {science} english = {english} gujarati = {gujarati} hindi = {hindi} computer = {computer}")
    total = maths + science + english
    return total 

m = int(input("Enter marks for Maths: "))
s = int(input("Enter marks for Science: "))
e = int(input("Enter marks for English: "))
g = int(input("Enter marks for Gujarati: "))
h = int(input("Enter marks for Hindi: "))
c = int(input("Enter marks for Computer: "))

# total = getMerit(g,h,c,m,s,e)
total = getMerit(computer=c,hindi=h,gujarati=g,english=e,science=s,maths=m)
print(f" total = {total}")

