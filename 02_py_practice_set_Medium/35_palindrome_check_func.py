# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:22:19 2024

@author: user
"""

# =============================================================================
# check if given string and number is palindrome 
# =============================================================================

def palindrome_check_func(x):
    try:
        x=str(x)
        if x[::-1]==x:
            return f'{x} is palindrome'
        else:
            return f'{x} is not palindrome'
    except Exception as e :
        return f'check your input type,it should be string {e}'
        
    
result = palindrome_check_func('nitin')
print(result)