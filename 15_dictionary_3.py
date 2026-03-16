student = ['name','dob','gender','weight','rollno']
print(student)

#create dictionary which must have name, dob gender weight and rollno as key
rahul = dict.fromkeys(student)
sita = dict.fromkeys(student)

print(rahul)
print(sita)

#uodate dictionary using dictionary method
rahul.update({'name':'rahul','dob':'2000-12-31','gender':True,'weight':75.11,'rollno':100,'city':'bhavnagar'})

#updating individual key 
sita['name'] = 'Sita'
sita['dob'] = '2010-05-25'
sita['gender'] = False 
sita['city'] = 'rajkot' 

print(rahul)
print(sita)

#remove last key value pair 
sita.popitem()
#remove specific key and its value 
sita.pop('weight')
sita.pop('rollno')
print(sita)

#display keys
print(rahul.keys())

#display values 
print(rahul.values())


#display items
print(rahul.items())

#get value of name
print(rahul.get('name')) #rahul
print(rahul.get('dob')) # 2000-12-31
print(rahul.get('email','not found')) #not found
print(rahul['gender']) #true
# print(rahul['pincode']) #Error
print(rahul.get('pincode')) #None

# rahul2 = rahul #wrong way of copying dictionary
rahul2 = rahul.copy() #perfect way
print(rahul2)
rahul.clear()
print(rahul2)