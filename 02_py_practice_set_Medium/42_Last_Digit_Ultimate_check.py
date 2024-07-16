# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:57:21 2024

@author: user
"""

# =============================================================================
'''
Your job is to create a function, that takes 3 numbers: a, b, c 
and returns True if the last digit of a * b = 
the last digit of c.
'''
# =============================================================================

def Last_Digit_Ultimate_check(a,b,c):
    a=str(a)
    b=str(b)
    c=str(c)
    multiple_a_b=int(a[-1]) * int(b[-1])
    multiple_str=str(multiple_a_b)
    if int(multiple_str[-1]) == int(c[-1]):
        return True
    return False

result=Last_Digit_Ultimate_check(12,215,2142)
print(result)
