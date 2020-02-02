#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Мега глупая сортировка. Досчитывает до конца, не зная, что уже придется перетряхивать массив на i шаге
"""
import numpy as np
from time import time
t0 = time


def silly_random_sort (q):
    a = []
    for iter in range (len(q)-1):
        if q[iter] <= q[iter+1]: 
            a = np.append(a, 1)
        else:
            a = np.append(a, 0)
    return a


array =  np.random.randint(1, 1000, 10)


while np.sum(silly_random_sort (array))!= len(array)-1:
    np.random.shuffle (array)
    silly_random_sort (array)    



print(time()-t0)              

#%% 
'''
2. Более умная случайная сортировка. Заметив, что придется перетряхивать массив, останавливается, 
перетряхивает и начинает заново проверять на соответствие расположениям отсортированности
'''


from time import time 
t0 = time()
    
array =  np.random.randint(1, 10000, 10)


def smart_random_sort (q):
    for iter in range (len(q)-1):
        if q[iter] > q[iter+1]:
            return 0
            break
    return 1


def shuffle (q):
    while smart_random_sort (q) !=1:
        np.random.shuffle (q)
        smart_random_sort (q)
    return q


shuffle (array)
print(time()-t0)

#%%
"""Проверить : лучше ли первое перетряхивание массива при случайной сортировке, чем второе"""


array =  np.random.randint(1, 200, 10)


def sh (q):
    y = np.copy(q)
    np.random.shuffle(y)
    return y


def sort_depth (q):
    a_1 = sh (q) 
    a_2 = sh (q)
    return a_1, a_2


a1, a2 = sort_depth (array)


def comparison (a_1, a_2):
    a_1w = []
    for iter in range (len(a_1)):
        if a_1[iter] < a_2[iter]:
            a_1w = np.append(a_1w, 1)
        else:
            a_1w = np.append(a_1w, 0)
    if np.sum(a_1w) < len(a_1)/2:
        print('Рандомная сортировка 2 лучше')
    else:
        print('Рандомная сортировка 1 лучше')
    return a_1w


a1w = comparison (a1, a2)
                



