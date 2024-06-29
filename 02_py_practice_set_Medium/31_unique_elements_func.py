# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:49:32 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:24:58 2024

@author: user
"""

# =============================================================================
# Two Distinct Elements
# In each input list, every number repeats at least once,
#  except for two. Write a function that returns the two unique numbers.
# =============================================================================


list1=[9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]

def unique_elements_func(n):
    unique_elements=[]
    elements_dict={}
    Two_Distinct_Elements=[]
    
    for x in list1:
        if x not in unique_elements:
            unique_elements.append(x)
            elements_dict[x]=0
        if x in unique_elements:
            elements_dict[x] += 1
    
    for x,y in elements_dict.items():
        if y==1 :
            Two_Distinct_Elements.append(x)
    
    return Two_Distinct_Elements

result=unique_elements_func(list1)
print(result)
            