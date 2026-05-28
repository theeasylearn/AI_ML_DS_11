import pandas as pd 

#1d series 
s1 = pd.Series([3,-2,1,-4,5],index=['a','b','c','d','e'],name='my series')


print(s1.abs())
print(s1.idxmin()) # d
print(s1.idxmax()) # e
print(s1.min())
print(s1.max())
print("Size of the series",len(s1))
print(s1.sort_values())
print(s1.sort_index())
