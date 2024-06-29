# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:02:35 2024

@author: user
"""

list_1=[[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]

def Sum_fractions_func(n):
    sum_fractions=0
    for x in list_1:
        y = round(x[0] / x[1])
        sum_fractions +=y

    return sum_fractions
        
result=Sum_fractions_func(list_1)
print(result)
        