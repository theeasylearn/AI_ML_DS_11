import numpy as np 

num = int(input("Enter seeds"))
np.random.seed(num)

print(np.random.rand(5,5))
print(np.random.randint(1,10,5))
print(np.random.uniform(0,1,3))

list = [10,20,30,40,50]
array1 = np.array(list)

print(np.random.choice(array1))

#array shuffle
np.random.shuffle(array1)
print(array1)