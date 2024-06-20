# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:13:27 2024

@author: user
"""

# =============================================================================
'''
Python got drunk and the built-in functions str() and int() are acting odd:

str(4) ➞ 4
str("4") ➞ 4
int("4") ➞ "4"
int(4) ➞ "4"

You need to create two functions to substitute str() and int().
A function called int_to_str() that converts integers into strings 
and a function called str_to_int() that converts strings into integers.
'''
# =============================================================================


def intTostr_and_strTo_int_convertor_func(a):
    if type(a) == str:
        Output_int=int(a)
        return Output_int
    elif type(a)==int:
        Output_str =str(a)
        return Output_str
    else:
        ValueError(f"{a} should be only int or str type")


intTostr_and_strTo_int_convertor_func('4')
        
