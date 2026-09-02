import numpy as np 
from sklearn.linear_model import LinearRegression

#create dataset (convert list into numpy array)
house_info = np.array([
    [1000, 2],
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 4]
])
#output dataset
price = np.array([50, 58, 75, 88, 100])

#create model 
model = LinearRegression()

#model train 
model.fit(house_info,price)

#prediction 
house = np.array([[2000,6]])
print("price of house with 2000 Sq feet and 6 bedroom are ",model.predict(house))

house_2 = np.array([[200,2]])
print("price of house with 200 Sq feet and 2 bedroom are ",model.predict(house_2))


