import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

#create dataset 
X = np.array([[20.00],[20.14],[20.28],[20.42],[20.57],[20.71],[20.85],[20.99],[21.13],[21.27],[21.41],[21.56],[21.70],[21.84],[21.98],[23.09],[24.36],[25.64],[26.91],[28.18],[29.45],[30.73],[32.00],[33.27],[34.55],[35.82],[37.09],[38.36],[39.64],[40.25],[40.61],[40.96],[41.31],[41.67],[42.02],[42.37],[42.73],[43.08],[43.43],[43.79],[44.14],[44.49],[44.85],[45.20],[45.56],[45.91],[46.26],[46.62],[46.97],[47.32],[47.68],[48.03],[48.38],[48.74],[49.09],[49.44],[49.80],[50.61],[52.02],[53.43],[54.85],[56.26],[57.68],[59.09],[60.51],[61.92],[63.33],[64.75],[66.16],[67.58],[68.99],[70.10],[70.45],[70.81],[71.16],[71.52],[71.87],[72.22],[72.58],[72.93],[73.28],[73.64],[73.99],[74.34],[74.70],[75.05],[75.40],[75.76],[76.11],[76.46],[76.82],[77.17],[77.53],[77.88],[78.23],[78.59],[78.94],[79.29],[79.65],[80.00]])

model = KMeans(n_clusters=3,random_state=42,n_init=5)

#train model 
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centeriods 
print(model.cluster_centers_)

#display data
customers = ["Aarav", "Aditi", "Rohan", "Priya", "Arjun", "Neha", "Rahul", "Sneha", "Vikram", "Pooja", "Karan", "Ananya", "Rajesh", "Kavita", "Amit", "Nisha", "Suresh", "Riya", "Manish", "Divya", "Akash", "Simran", "Nitin", "Pallavi", "Ravi", "Shreya", "Vivek", "Isha", "Sanjay", "Meera", "Harsh", "Komal", "Deepak", "Swati", "Yash", "Tanvi", "Prakash", "Anjali", "Mohit", "Payal", "Abhishek", "Kajal", "Rakesh", "Mansi", "Dhruv", "Sonal", "Pankaj", "Bhavna", "Kunal", "Radhika", "Vishal", "Nandini", "Sameer", "Het", "Preeti", "Gaurav", "Monika", "Chirag", "Jinal", "Tarun", "Rupal", "Jay", "Khushi", "Ankit", "Ritika", "Mihir", "Poonam", "Dev", "Sakshi", "Aakash", "Bhumi", "Nirav", "Shruti", "Rajiv", "Ayesha", "Imran", "Farhan", "Zoya", "Adil", "Fatima", "Rohit", "Lakshmi", "Siddharth", "Kavya", "Vijay", "Srinivas", "Keerthi", "Manoj", "Swetha", "Arun", "Deepa", "Karthik", "Harini", "Pranav", "Anusha", "Sanjana", "Varun", "Ishaan", "Muskan", "Parth", "Nikita", "Devanshi"]

for customer,spending,label in zip(customers,X.flatten(),labels):
    if label == 0:
        message = "low spending"
    elif label == 1:
        message = "highest spending"
    else:
        message = "medium spending"
    print(f"Name : {customer} spending score = {spending} label = {message}")

#create chart
plt.scatter(labels,X,s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Spending score")
plt.xlabel("Labels")
plt.show()


