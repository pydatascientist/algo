'''
Iris clusterisation
'''
#Downloading data from educational website. You can also use scikit-learn datasets.
from urllib.request import urlretrieve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn import metrics
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.preprocessing import StandardScaler

iris = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
urlretrieve(iris)
df = pd.read_csv(iris, sep=',', header=None)
df = df.rename(columns = {0:"sepal_length", 1:"sepal_width", 2:"petal_length", 3:"petal_width", 4:"class"})

#%%
df_m = df.iloc[:, lambda df: [0,1,2,3]]

for iter in range (10):
    df_m = pd.concat([df_m, df_m])

#%%
df_m = df_m + np.random.rand(len(df_m),4)


#%% 
'''Вычисляем коэффициенты силуэта для определения количества необходимых кластеров. Кластеризацию проведем двумя
#способами : KMeans и DBSCAN. Кластеризацию проводим 150 раз'''

for iter in range (8):
    globals()['cluster_'+str(iter+2)] = [2 + iter]


for iter in range (8):
    globals()['silhouette_'+str(iter+2)] = pd.DataFrame(columns = [iter+2])

#%% Кластеризация методом KMeans
def silhouette_cluster_definer_KMeans(cluster_num, silhouette_num):
    for i in range (150):
        df_sample = df_m.sample(150)
        for n_clusters in cluster_num:
            model = KMeans (n_clusters=n_clusters)
            cluster_labels = model.fit_predict(df_sample)
            silhouette = silhouette_score(df_sample, cluster_labels, sample_size = 100)
            silhouette_num.loc[i] = silhouette
        i+=1

            
#%%
silhouette_cluster_definer_KMeans (cluster_2, silhouette_2)
silhouette_cluster_definer_KMeans (cluster_3, silhouette_3)
silhouette_cluster_definer_KMeans (cluster_4, silhouette_4)
silhouette_cluster_definer_KMeans (cluster_5, silhouette_5)
silhouette_cluster_definer_KMeans (cluster_6, silhouette_6)
silhouette_cluster_definer_KMeans (cluster_7, silhouette_7)
silhouette_cluster_definer_KMeans (cluster_8, silhouette_8)
silhouette_cluster_definer_KMeans (cluster_9, silhouette_9)

#%%
silhoette_KMeans = pd.concat([silhouette_2, silhouette_3, silhouette_4,
                              silhouette_5, silhouette_6, silhouette_7,
                              silhouette_8, silhouette_9], axis = 1)
#%%
#Математическое ожидание коэффициента силуэта
mean = silhoette_KMeans.mean().plot.bar(sharex = True, sharey = True)


#%%
'''
По итогам кластеризации методом KMeans получена следующая картина:
Равномерное убывание силуэтного коэффициента начинается с 3 кластера. Целесообразно отбросить второй кластер из рассмотрения
В дальнейшем на этой же выборке проведем кластеризацию методом DBSCAN.
Запустим алгоритм DBSCAN для предсказания количества кластеров.
'''


df_sample = df_m.sample(150)
dbscan = DBSCAN(eps=0.3, min_samples=10).fit(df_sample)
labels = dbscan.labels_
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
#%%
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Silhouette Coefficient: %0.3f"% metrics.silhouette_score(df_sample, labels))


#%%
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()