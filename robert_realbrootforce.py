'''
Решение задачи donald + gerald = robert путем brootforce. 
counter_stop можно установить самостоятельно. 
Время реализации задачи увеличивается пропорционально количеству повторений
Рекомендуемое значение counter_stop = 100000000
'''
from time import time
t0 = time()
import numpy as np
import pandas as pd

d=5
i=0
t=0
counter=0
counter_stop=1000000
results=pd.DataFrame(columns=['O','N','A','L','E','R','G','B'], index=[i])
while counter<counter_stop:
    o=np.random.randint(0,10)
    n=np.random.randint(0,10)
    a=np.random.randint(0,10)
    l=np.random.randint(0,10)
    e=np.random.randint(0,10)
    r=np.random.randint(0,10)
    g=np.random.randint(0,10)
    b=np.random.randint(0,10)
    if (d+d)*1 + (l+l)*10 + (a+a)*100 + (n+r)*1000 + (o+e)*10000 + (d+g)*100000 == t*1 + r*10 + e*100 + b*1000 + o*10000 + r*100000:
        results.loc[i]=[o,n,a,l,e,r,g,b]
        i+=1
        counter+=1
    else:
        counter+=1
print(results)
print(time()-t0)

