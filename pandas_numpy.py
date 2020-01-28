#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Pandas 37. Исходная задача
t0 = time()
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv')
 
# Формат каждого столбца
print('\n', 'Формат столбцов:')
print(df.dtypes)
 
# Размерность DataFrame
print('\n', 'Размерность:')
print(df.shape)
 
# Общая статистика
print('\n', 'Общая статистика')
print(df.describe())

print(time()-t0)

С параллелизацией немного быстрее (примерно на 20%), но заметно только на сервере Jupyter.

'''

import multiprocessing.dummy as mp
from time import time
import pandas as pd

t0  = time()

def proc_0 ():
    global df 
    df = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv')
    print('\n', 'Общая статистика')
    print(df.describe())

def proc_1():
    print('\n', 'Формат столбцов:')
    print(df.dtypes)
    
    
def proc_2():
    print('\n', 'Размерность:')
    print(df.shape) 
    
p = mp.Pool(processes = 3)

if __name__== '__main__':
    results = p.map(lambda f: f(),[proc_0, proc_1, proc_2])
    print(results)
    p.close()
    p.join()

print(time() - t0)
 
#%%
'''Numpy 26. Исходная задача
t0 = time()
Z = np.linspace(0,9,120000000)[1:-1]
print(Z)
print(time()-t0)

'''

from multiprocessing import Process
from time import time
import numpy as np

t0 = time()
    
def vector(num):
    Z = np.linspace(0,9,num)[1:-1]
    print(Z)
    
if __name__ == '__main__':
    p = Process(target=vector, args = (120000000,))
    p.start()
    print(time()-t0)
    p.join()
    


#%%





#%%
'''
Numpy 27. Исходная задача
Z = np.random.random(1000)
Z.sort()
print(Z)
При количестве рандомных наблюдений 10 (как в исходной задаче) имеем превосходство обычного метода
нампай над параллелизацией.
При использовании 1000 наблюдений с параллелизацией примерно в 3 раза быстрее.
'''
from multiprocessing import Process
import numpy as np
t0 = time()

def rand (num):
    Z = np.random.random(num)
    Z.sort()
    print(Z)
    
if __name__ == '__main__':
    p = Process(target=rand, args = (1000,))
    p.start()
    print(time()-t0)
    p.join()
    
#%%
''' Numpy 28. Исходная задача
from time import time
t0  = time()
A = np.random.randint(0,2,1000000)
B = np.random.randint(0,2,1000000)
equal = np.allclose(A,B)
print(equal)
print(time()-t0)

Эмпирически: при количестве наблюдений менее ~10**6, массивы нампай показывают лучший по времени 
результат. При раскладе, который расписан внизу, мультипроцессинг примерно в 10 раз быстрее обычного
метода numpy без дополнительной параллелизации.
'''

from multiprocessing import Process
import numpy as np
t0 = time()

def creator (num):
    A = np.random.randint(0,2,num)
    B = np.random.randint(0,2,num)
    equal = np.allclose(A,B)
    print(equal)
    
if __name__ == '__main__':
    p = Process(target=creator, args = (1000000,))
    p.start()
    print(time()-t0)
    p.join()   
    
    
#%%


#%%
'''Numpy 29. Исходная задача
Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1

Присвоение переменной Z атрибута неизменяемости происходит за считанные доли милисекунд.
При этом, изменение размера вектора не сильно влияет на скорость решения задачи, т.к. 
судя по всему, массивы numpy используют параллелизацию при большом количестве наблюдений.
Параллелизация путем Process и Pool здесь увеличивает общее время получения результата примерно в 10 раз
вне зависимости от количества используемых процессоров.
'''


from multiprocessing import Process
import numpy as np
from time import time
t0 = time()

def s (num):
 Z = np.zeros(num)
 Z.flags.writeable = False
 Z[0] = 1

    
if __name__ == '__main__':
    p = Process(target=s, args = (10,))
    p.start()
    print(time()-t0)   
    p.join()   
 
    






