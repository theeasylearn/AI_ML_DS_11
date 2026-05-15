#create list 
cars = ['Maruti','Tata','Mahindra','Hundai','Honda']
print(cars) #print whole list 
#print 1st car name
print(cars[0])

print(cars[2]) #mahindra
# print(cars[6]) # error
#change 3rd car name 
cars[2] = "Kia"
print(cars)

#delete 3rd car 
del cars[2]
print(cars)

#delete whole list 
del cars 
print(cars)