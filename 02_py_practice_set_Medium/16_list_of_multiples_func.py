# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:55:45 2024

@author: user
"""

# =============================================================================
# Create a function that takes two numbers as arguments (num, length) 
# and returns a list of multiples of num until the list length reaches length.
# ist_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
# =============================================================================

def list_of_multiples_func(num,length):
    list_of_multiples=[]
    for x in range(1,length+1):
        a=num*x
        list_of_multiples.append(a)
    return f'list_of_multiples is {list_of_multiples}'

result = list_of_multiples_func(12,10)
print(result)

    