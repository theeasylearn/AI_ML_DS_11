def getnsquare(x,y=2):
    print(f"x = {x} y = {y}")
    result = (x * x) + (2 * x * y) + (y * y)
    return result 

x = int(input("enter value for x"))
y = int(input("enter value for y"))

result = getnsquare(x,y)
print("result with 2 argument = ",result)

result = getnsquare(x)
print(f"result with one argument {x} = ",result)