# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:04:42 2024

@author: user
"""

# =============================================================================
# Check if a year is leap year or not
# =============================================================================

def leap_year_check_func(x):
    if x % 100 ==0:
        if x % 400 ==0:
            return f'{x} is a leap year'
    elif x % 4==0:
        return f'{x} is a leap year'
    else:
        return f'{x} is not a leap year'
        
result = leap_year_check_func(2000)
print(result)
    
            