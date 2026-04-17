import random as rd 
import string as st 
#global variable
seeds = st.digits + st.printable
def generatePassword(length=10):
    global seeds
    temp = list(seeds)
    rd.shuffle(temp)
    password = ''.join(temp[0:10])
    return password

password = generatePassword()
print(password)

password = generatePassword(12)
print(password)