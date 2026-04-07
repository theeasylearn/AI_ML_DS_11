# 1	 Without return value without argument
def printLine():
    print("-"*100)
# 2	Without return value with argument 
def printCenter(text):
    print(text.center(100))

# 3	 With return value without argument
def getPi():
    pi = 22/7
    return pi 
printLine()
text = "THE EASYLEARN ACADEMY"
printCenter(text)
printLine()
pi = getPi()
print(f"value of pi {pi:.2f}")