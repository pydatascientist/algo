'''
Iris correlation. First thing to plot and look at how they're distributed before clasterisation
'''
#Downloading data from educational website. You can also use scikit-learn datasets.
from urllib.request import urlretrieve
import pandas as pd
iris = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
urlretrieve(iris)
df = pd.read_csv(iris, sep=',', header=None)
df = df.rename(columns = {0:"sepal_length", 1:"sepal_width", 2:"petal_length", 3:"petal_width", 4:"class"})

#Kendall corellation requires class name objects not to be str. Modify them to int by creating dict and mapping:
dic = dict(zip(['Iris-setosa','Iris-versicolor','Iris-virginica'],[10, 100, 1000]))
df['class'] = df['class'].map(dic)

matcorr_k = df.corr(method='kendall')
matcorr_s = df.corr(method='spearman')

#Pearson doesnot requires. 
matcorr_p = df.iloc[:, lambda df: [0,1,2,3]].corr(method = 'pearson')
