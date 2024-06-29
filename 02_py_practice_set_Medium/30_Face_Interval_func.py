# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:24:58 2024

@author: user
"""

# =============================================================================
# In mathematics, interval is the difference between the largest 
# number and the smallest number in a list.

# To illustrate:

# A = (3, 5, 7, 23, 11, 42, 80)

# Interval of A = 80 - 3 = 77
# Create a function that takes a list and returns ":)" 
# if the interval of the list is equal to any other element; 
# otherwise return ":(".

# =============================================================================

def Face_Interval(list_1):
    largest_num=1
    smallest_num=1
    
    if  type(list_1)==str:
        return (":/")
    else:
        for x in list_1:
            
            if largest_num < x:
                largest_num=x
            if smallest_num > x:
                smallest_num = x
            
        interval= largest_num-smallest_num
        
        if interval in list_1:
            return (':)')
        else:
            return (':(')
        
result=Face_Interval("bruh")
print(result)
            
            