# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:34:17 2024

@author: user
"""
# =============================================================================
# Write a function that accepts the height and width (m, n) and 
# an optional proc s and generates a list with m elements. Each element 
# is a string consisting of either:

# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.
# =============================================================================
        

def make_rug_func(height, width, sign='#'):
    result_list = []
    for x in range(height):
        line = sign * width
        result_list.append(line)
        print(line)
    return result_list

rug = make_rug_func(3, 5, '#')
print(rug)
    