import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create customer dataset
# ============================================

data = {
    "Customer": [
        "C1", "C2", "C3",
        "C4", "C5", "C6",
        "C7", "C8", "C9",
        "C10", "C11", "C12"
    ],

    "AnnualIncome": [
        15, 18, 20,
        45, 48, 50,
        80, 85, 90,
        30, 33, 35
    ],

    "Purchases": [
        3, 4, 5,
        10, 11, 12,
        20, 21, 22,
        7, 8, 8
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "AnnualIncome",
    "Purchases",
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled,method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage,labels=df["Customer"].values)

plt.title("Hierarchical Clustering Dendrogram - Ward Method")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()



model = AgglomerativeClustering(n_clusters=4,linkage="ward")
model.fit_predict(x_scaled)

print(model.labels_)
df['clusters'] = model.labels_
print(df)

#create chart
plt.figure(figsize=(10,8))
plt.title("agglomerative hierarchical clustering")
plt.scatter(df['AnnualIncome'],df['Purchases'],c=df['clusters'])
plt.xlabel("Annual Income")
plt.ylabel("Purchases")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index,'Customer'],(
        df.loc[index,'AnnualIncome'],
        df.loc[index,'Purchases']
    ),xytext=(5,5),textcoords="offset points")
plt.show()
exit()
