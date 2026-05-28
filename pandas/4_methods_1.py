import pandas as pd 

#1d series 
s1 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],name='my series')

print(s1.head(2)) # 1, 2
print(s1.tail(2)) # 4, 5
print(s1.to_list())
print(s1.to_dict())
print(type(s1)) 
print(s1.describe())

