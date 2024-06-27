# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:06:57 2024

@author: user
"""

# =============================================================================
# Write a function that inverts the keys and values of a dictionary.

# Examples
# invert({ "z": "q", "w": "f" })
# ➞ { "q": "z", "f": "w" }
# =============================================================================

# Invert Keys and Values

invert_dict={ "a": 1, "b": 2, "c": 3 }

def Invert_Keys_and_Values(invert_dict):
    inverted_dict={}
    for key,values in invert_dict.items():
        inverted_dict[values]=key
    return inverted_dict


Invert_Keys_and_Values(invert_dict)
    

    
    
