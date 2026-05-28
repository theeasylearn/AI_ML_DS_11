import pandas as pd 

#create series 
s1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'],name='my series')
print(s1)

#get value by index 
print("value at label a = ",s1.loc['a'])

#update value by index 
s1.loc['b'] = 200
print(s1)

#access value by position
print("value at position 3 = ",s1.iloc[2])

#change value by position
s1.iloc[2] = 300
print("updated value at position 3 = ",s1.iloc[2])


# print("x = ",s1.loc['x']) #unsafe becuase it generate key eror if no label x 
print("value at label x = ",s1.get('x',0)) #safe because it return 0 if no label x 


