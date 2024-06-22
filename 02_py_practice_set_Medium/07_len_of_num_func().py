# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:16:32 2024

@author: user
"""

# =============================================================================
'''
Create a function that takes a number num and returns its length.
'''
# =============================================================================

def len_of_num_func(n):
    try:
        n2=str(n)
        len_of_num=0
        for x in n2:
            len_of_num +=1
        return len_of_num
    except Exception as e :
        print(f'Got an error as {e}')

result=len_of_num_func(1000000)
print(f'length of given num is {result}')


# =============================================================================
''' 2nd method'''
# =============================================================================

def len_of_num_func2(n):
    n=str(n)
    return len(n)

result2=len_of_num_func2(100)
print(f'length of given result {result2}')

