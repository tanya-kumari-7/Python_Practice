# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:12:56 2024

@author: user
"""

# =============================================================================
# Create a Fibonacci sequence
# =============================================================================

def Fibonacci_sequence(num):
    Fibonacci_list=[1,0]
    for x in range(1,num-1):
        next_num=Fibonacci_list[-1]+Fibonacci_list[-2]
        Fibonacci_list.append(next_num)
    return Fibonacci_list

result = Fibonacci_sequence(15)
print(result)
    
