import numpy as np 
list = [
        [[10,20,30],[40,50,60]],
        [[11,22,31],[41,51,61]],
        [[71,81,91],[140,150,160]]
        ]
array_3d = np.array(list,dtype=np.int16)
print(array_3d)
print("No of Dimensions ",array_3d.ndim)
print("Size of the array in bytes",array_3d.nbytes)
print("Size of the element in array",array_3d.itemsize)
print("Data type in array",array_3d.dtype)
print("No of elements in array ",array_3d.size)
print("Shape of array ",array_3d.shape)
print(array_3d.T)

