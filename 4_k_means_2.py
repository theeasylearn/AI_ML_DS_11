import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# STEP 1: load dataset
df = pd.read_csv("area_orders_data.csv")
# select input features
X = df[
    [
        "Distance",
        "DailyOrders",
    ]]
# print(X)

#apply scaler 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# print(X_scaled)
#use elbow method to decide k 
inertia = []
for i in range(1,7):
    model = KMeans(n_clusters=i,random_state=42,n_init=10)
    model.fit(X_scaled)
    calculated_inertia = model.inertia_
    inertia.append(calculated_inertia)
plt.plot(range(1,7),inertia)
plt.xlabel("inertia",)
plt.ylabel("clusters")
plt.show()
model = KMeans(n_clusters=3,random_state=42,n_init=10)
#train model
model.fit(X_scaled)
labels = model.labels_
print(labels)
df['label'] = labels
print(df)