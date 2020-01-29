#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Рексурсия способ 2
'''
import numpy as np

def recursion(data, size):
   if size == 0:
     return 0
   else:
     return data [size-1] + recursion (data, size-1)

a = np.arange(101)
b = recursion(a,100)
print (b)