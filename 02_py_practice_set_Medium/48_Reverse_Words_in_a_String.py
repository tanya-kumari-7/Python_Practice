# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 23:27:26 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:47:21 2024

@author: user
"""
# =============================================================================
'''
Given an input string, reverse the string word by word.
'''
# =============================================================================

def Reverse_Words_in_a_String(string):
    string2 = string.split()  
    new_string = ' '.join(string2[::-1])
    return new_string

result=Reverse_Words_in_a_String("  hello world!  ")
print(result)  
    