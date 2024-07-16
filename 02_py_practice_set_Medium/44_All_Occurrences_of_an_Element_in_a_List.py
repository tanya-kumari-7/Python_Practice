# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:57:12 2024

@author: user
"""

# =============================================================================
'''
All_Occurrences_of_an_Element_in_a_List

Create a function that returns the indices of all 
occurrences of an item in the list.
'''
# =============================================================================

def All_Occurrences_of_an_Element_in_a_List(enter_list,item):
    indices_list=[]
    for indices,value in enumerate(enter_list):
        if value ==  item:
            indices_list.append(indices)
    return f'{indices_list}'
        
result=All_Occurrences_of_an_Element_in_a_List([1, 5, 5, 2, 7], 7)
print(result)        

