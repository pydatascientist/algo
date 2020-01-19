'''
Сложение 100 чисел по схеме фон - Неймана
1. Делим выборку на 2 части до тех пор, пока не получим 1 число
'''

import numpy as np
from time import time
counter = 0
numpy = 0
fon_neyman = 0

while counter < 100000:
    t1 = time()
    data = np.arange(101)
    np.sum(data)
    t1 = time()-t1
    
    t0 = time()
    def divider(data):
        d = len(data) // 2
        if len(data) != 1:
            sum_1 = divider(data[:d])
            sum_2 = divider(data[d:])
            return sum_1 + sum_2
        elif len(data):
            return (data[0])
    
    data = np.arange(101)
    sum  = divider(data)
    t0 = time() - t0
    
    if t0 < t1 :
        fon_neyman +=1
    elif t0 > t1:
        numpy +=1
    print(counter)
    counter+=1

print((fon_neyman*100/counter),'- Процент успешности алгоритма фон - Неймана')
print((numpy*100/counter),'- Процент успешности Numpy')
        
        
        



