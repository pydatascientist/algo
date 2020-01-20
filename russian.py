

'''
Решение задачи Даниил + Кирилл = Герман путем brootforce. 
counter_stop можно установить самостоятельно. 
Время реализации задачи увеличивается пропорционально количеству повторений
Рекомендуемое значение counter_stop = 100000000
'''
a1 = 'Даниил'.upper()
a2 = 'Кирилл'.upper()
a3 = 'Герман'.upper()

a = set(a1 + a2 + a3)
#%%
from time import time
t0 = time()
import numpy as np
import pandas as pd
j = 0

counter=0
counter_stop=10000000
results=pd.DataFrame(columns=['А', 'Г', 'Д', 'Е', 'И', 'К', 'Л', 'М', 'Н', 'Р'], index=[j])
while counter< counter_stop:
    a = np.random.randint(0,10)
    g = np.random.randint(0,10)
    d = np.random.randint(0,10)
    e = np.random.randint(0,10)
    i = np.random.randint(0,10)
    k = np.random.randint(0,10)
    l = np.random.randint(0,10)
    m = np.random.randint(0,10)
    n = np.random.randint(0,10)
    r = np.random.randint(0,10)
    if (l+l)*1 + (i+l)*10 + (i+i)*100 + (n+e)*1000 + (a+i)*10000 + (d+k)*100000 ==  n*1 + a*10 + m*100 + r*1000 + e*10000 + g*100000 :
        results.loc[j]=[a,g,d,e,i,k,l,m,n,r]
        j+=1
        counter+=1
    else:
        counter+=1
print(results)
print(time()-t0)

