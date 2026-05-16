import numpy as np 

#create array using zero 
array1 = np.zeros(5)

#create 2d array 
array3 = np.zeros([2,3],dtype=int)

#create array using one 
array2 = np.ones(5)

#create 2d array 
array4 = np.ones([3,2])

print(array1,array2,array3,array4)
print(array1.shape,array2.shape,array3.shape,array4.shape)

array3[0][0] = 100
array3[0][1] = 200
print(array3)
