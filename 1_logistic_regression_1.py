# import library 
import numpy as np 
from sklearn.linear_model import LogisticRegression

#create input dataset 
study_hours = np.array([[1],[1.5],[2],[2.5],[3],[3.5],[4],[5],[6],[7]])

#create output dataset
result = np.array([0,0,0,0,0,1,1,1,1,1])


#create model 
model = LogisticRegression()

print("model training started.....")
#model train 
model.fit(study_hours,result) # input, label (output)

print("model training complete.....")

#prediction 
divya = np.array([[8.3]])
prediction = model.predict(divya)

print("Divya pass fail prediction ",prediction)

#probability 
print("Divya pass fail prediction probability ",model.predict_proba(divya))

kashish = np.array([[3.25]])
prediction = model.predict(kashish)

print("kashish pass fail prediction ",prediction)

#probability 
print("kashish pass fail prediction probability ",model.predict_proba(kashish))


#accuracy 
print("Model accuracy = ",model.score(study_hours,result))