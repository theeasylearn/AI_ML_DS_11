import numpy as np 
list_1 = [[10,20,30,40,50]]
list_2 = [[10,20,30,40,50],[60,70,80,90,100]]
#convert array 
array_1d = np.array(list_1)
array_2d = np.array(list_2)
#array copy 
array_3 = np.copy(array_1d)
array_4 = np.copy(array_2d)
array_1d = np.array([])
array_2d = np.array([])
print(array_3)
print(array_4)
