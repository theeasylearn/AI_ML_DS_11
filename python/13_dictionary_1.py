#Dictionary
teacher = {'name':'ankit','surname':'patel','age':42,'gender':True,'dob':12.7,'secret':None}
print(teacher)

#update key value pair
teacher['secret'] = 123123

#add new key value pair 
teacher['city'] = "bhavnagar"
teacher['pincode'] = 364001

print(teacher)

#delete key value pair
del teacher['secret']

print(teacher)