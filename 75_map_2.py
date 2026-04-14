numbers1 = [10,20,30,40,150]
numbers2 = [5,25,9,50,100]

#make sum of both list into another list 
sum = map(lambda num1,num2: num1 + num2,numbers1,numbers2)
print("sum of both list ",list(sum))


#copy maximum value item by item 
maximum = map(lambda num1,num2: num1 if num1>num2 else num2,numbers1,numbers2)
print(list(maximum))