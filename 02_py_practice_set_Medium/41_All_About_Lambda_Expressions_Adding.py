# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:57:25 2024

@author: user
"""

# =============================================================================
'''
Write a function that returns a lambda expression, 
which adds n to its input
'''
# =============================================================================

def adds_n(n):
    return lambda x:x+n

object_=adds_n(11)
print(object_(10))


