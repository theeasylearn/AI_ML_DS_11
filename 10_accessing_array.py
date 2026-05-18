import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)

#print 1st column in all row 
print(arr[:,0])

#print all column in 1st row 
print(arr[0,:])

print("-"*100)
#filter array get value above 30
print(arr[arr>30])
#filter array get value above 30 and below 50
# print(arr[arr>30 and arr <50]) error because we can give at most 1 condition