# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:53:36 2024

@author: user
"""

def prime_num_check_func(num):
    for x in range(2, num):
        if num % x == 0:
            return f'{num} is not prime'
            break
    else:
        return f'{num} is prime'
    
result = prime_num_check_func(10)
print(result)
