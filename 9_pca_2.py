import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
df = None 
def do_pca():
    global df 
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "harrywang/wine-dataset-for-clustering",
        "wine-clustering.csv",
    )
    print("Size of dataset", df.shape)

    # Scale
    x_scaled = StandardScaler().fit_transform(df)

    # PCA with 7 components
    model = PCA(n_components=7)
    data = model.fit_transform(x_scaled)          # <- transformed data, not the model

    print("Explained variance ratio:", model.explained_variance_ratio_.sum().round(3))

    pca_df = pd.DataFrame(data, columns=[f"PC{i}" for i in range(1, 8)])
    return pca_df
def do_keans():
    # Elbow method
    inertias = []
    k_values = range(2, 11)
    score = {}
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(pca_df)
        inertias.append(kmeans.inertia_)
        print(k, round(silhouette_score(pca_df,labels), 3))
        score[k] = round(silhouette_score(pca_df,labels), 3)

    print(score)
    no_of_clusters = max(score, key=score.get)
    KMeans(n_clusters=no_of_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(pca_df)
    df['clusters'] = labels
    print(df.head(50))

pca_df = do_pca()
do_keans()


# plt.plot(k_values, inertias, marker="o")
# plt.xlabel("Number of clusters (k)")
# plt.ylabel("Inertia")
# plt.xticks(k_values)
# plt.title("Elbow method")
# plt.show()

