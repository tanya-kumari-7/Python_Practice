# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:13:23 2024

@author: user
"""

# =============================================================================
# Write a function that transforms a list of characters into a list
 # of dictionaries, where:

# The keys are the characters themselves.
# The values are the ASCII codes of those characters.
# =============================================================================
list_char=["a", "b", "c"]
def Char_ASCII_dict_func(list_char):
    list_dic={}
    for x in list_char:
        list_dic[x]=ord(x)
    return list_dic

result=Char_ASCII_dict_func(list_char)
print(result)
