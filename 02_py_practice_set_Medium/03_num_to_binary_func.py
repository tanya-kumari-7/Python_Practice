# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:24:05 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:41:26 2024

@author: user
"""

# =============================================================================
'''
Convert number into binary
'''
# =============================================================================
# ===========================================================================



def num_to_binary_func(num):
    binary=''
    divide=num
    while divide != 0: 
        rem=divide%2
        divide=divide//2
        binary=str(rem)+binary
    print(binary)

num_to_binary_func(20)


    







