# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:52:02 2024

@author: user
"""

# =============================================================================
'''
Create a function that takes a dictionary of objects
 like { "name": "John", "notes": [3, 5, 4] } and 
 returns a dictionary of objects 
 like { "name": "John", "top_note": 5 }.
'''
# =============================================================================

dic={ 
     "name": "John", 
     "notes": [3, 5, 4] 
     }

def Get_Student_with_Names_and_Top_Notes(n):
    n['name']='JohnA'
    n['notes']= max(n['notes'])
    return n

result=Get_Student_with_Names_and_Top_Notes(dic)
print(f'{result}')