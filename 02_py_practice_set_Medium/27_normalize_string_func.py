# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:47:48 2024

@author: user
"""

# =============================================================================
# October 22nd is CAPS LOCK DAY. Apart from that day, 
# every sentence should be lowercase, so write a function to 
# normalize a sentence.

# Create a function that takes a string. If the string is all uppercase 
# characters, convert it to lowercase 
# =============================================================================

def normalize_string_func(x):
    return x.capitalize()

result=normalize_string_func("CAPS LOCK DAY IS OVER")
print(result)
    