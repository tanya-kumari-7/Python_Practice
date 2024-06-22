# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:06:04 2024

@author: user
"""
# =============================================================================
'''
Create a function that finds the highest integer in the list using recursion.
'''
# =============================================================================

num_list=[1,2,3,5,7,9,100,500]
def highest_num_func(n):
    highest_num_of_list=0
    for x in n :
        if x > highest_num_of_list:
            highest_num_of_list=x
            
    return highest_num_of_list
    

result=highest_num_func (num_list)
print(f'Highest number from the list is {result}')