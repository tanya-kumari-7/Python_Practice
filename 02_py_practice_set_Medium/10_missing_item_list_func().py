# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:20:45 2024

@author: user
"""

# =============================================================================
'''
our spouse is not concerned with the loss of material possessions 
but rather with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lowercase
 representing the name of the pet (e.g. "rambo"), return:

"Rambo is gone..." if the name is on the list.
"Rambo is here!" if the name is not on the list.
Note that the first letter of the name in the return statement 
is capitalized.
'''

# =============================================================================
items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50}

def missing_item_list_func(item):
    msg = ''
    if item in items.keys():
        item=item.capitalize()
        msg = f'{item} is gone'
        return msg
    else:
        msg = f'{item} is here'
        return msg
    
result2=missing_item_list_func('tv')
print(f'{result2}')
    
