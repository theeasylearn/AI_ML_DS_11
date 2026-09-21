import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
# 1. Download Chicago crime data
url ="https://data.cityofchicago.org/resource/ijzp-q8t2.csv?$limit=5000"

# load data
df = pd.read_csv(url)

#filter column 
X = df[
    ["latitude",
        "longitude"
    ]
]
#remove blank rows 
X = X.dropna()
print(len(X))
print(X.head(20))

#create model 
model = DBSCAN(min_samples=10,eps=0.0002)

#train model
model.fit_predict(X)

labels = model.labels_

#add labels into dataframe
X['labels'] = labels

print("Cluster wise count")
print(X['labels'].value_counts())
print(X.head(20))


#create scatter plot
plt.figure(figsize=(10,8))

#create chart 
plt.scatter(X['latitude'],X['longitude'],c=X['labels'],s=10)
plt.title("DBSCAN ")
plt.xlabel("latitude")
plt.ylabel("Longitude")
plt.grid(True)
plt.show()
