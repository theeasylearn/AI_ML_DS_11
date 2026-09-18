# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Grouping 12 Countries
# https://gist.github.com/theeasylearn/b64e79246d4691113a0a62939801db81
# ============================================================
# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ============================================================
# Step 2: Create the dataset
# ============================================================

data = {
    "Country": [
        "India",
        "China",
        "USA",
        "Germany",
        "Japan",
        "Brazil",
        "Canada",
        "Nigeria",
        "Switzerland",
        "Bangladesh",
        "Australia",
        "South Africa"
    ],

    # GDP per capita in USD
    "GDP_per_capita": [
        2700,
        13000,
        85000,
        55000,
        34000,
        11000,
        53000,
        1100,
        100000,
        2700,
        65000,
        6500
    ],

    # Life expectancy in years
    "Life_expectancy": [
        67,
        78,
        77,
        81,
        84,
        76,
        82,
        54,
        84,
        73,
        83,
        62
    ],

    # Internet users as percentage of population
    "Internet_usage": [
        55,
        76,
        97,
        92,
        87,
        81,
        94,
        36,
        96,
        45,
        97,
        75
    ]
}

#create dataframe
df = pd.DataFrame(data)
# print(df)

#select input features
X = df[
    [
        "GDP_per_capita",
        "Life_expectancy",
        "Internet_usage",
    ]
]

#scaling 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# print(X_scaled)

def devisive_clustering(X,countries,no_of_clusters=4):
    # print(X,countries,no_of_clusters)
    clusters = {
        0:list(range(len(countries)))
    }
    # print(clusters)
    next_key = 1
    while len(clusters)<no_of_clusters:
        #findout key with maximum sized list
        max_key = max(clusters, key=lambda cluster_id : len(clusters[cluster_id]))
        # print(max_key) # 0
        #get indexes
        indexes = clusters[max_key]
        #get data
        data = X[indexes]
        # print(data)
        #create model
        model = KMeans(n_clusters=2,random_state=2,n_init=10)
        model.fit_predict(data)
        labels = model.labels_
        # print(labels)
        list_1 = []
        list_2 = []
        for index,label in zip(indexes,labels):
            if label == 0:
                list_1.append(index)
            else: 
                list_2.append(index)
        # print(list_1,list_2)
        clusters[next_key] = list_1
        next_key=next_key+1
        clusters[next_key] = list_2
        next_key=next_key+1
        del clusters[max_key] 
        # print (clusters)
    return clusters
clusters = devisive_clustering(X_scaled,df['Country'].to_list(),4)
print(clusters)

#display cluster id and country name 
for cluster_id,indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        print(df.loc[index,"Country"])

df['cluster'] = 0
#add data into original dataframe 
for cluster_id,indexes in clusters.items():
    print(cluster_id)
    for index in indexes:
        df.loc[index,"cluster"] = cluster_id

print(df)

#display data as chart
plt.figure(figsize=(10,6))
plt.scatter(df["GDP_per_capita"],df["Life_expectancy"],c=df['cluster'],s=100)
#add lables for each c 
for i in range(len(df)):
    plt.annotate(df.loc[i,'Country'],(
        df.loc[i,"GDP_per_capita"],
        df.loc[i,"Life_expectancy"]
    ),xytext=(5,5),textcoords="offset points")

plt.title("Divisive clustering")
plt.xlabel("GDP per person")
plt.ylabel("Age ")
plt.show()