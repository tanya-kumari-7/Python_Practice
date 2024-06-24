# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:19:13 2024

@author: user
"""

# =============================================================================
# You are given two numbers a and b. Create a function that returns 
# the next number greater than a and b and divisible by b.
# =============================================================================

def Next_Num_GreaterThan_AandB_and_Divisible_by_B_func(num1,num2): 
    next_num=num2+1

    while True:
        if next_num % num2 == 0 and next_num > num1:
            break
        next_num+=1

    return f'Next Num Greater Than num1 and num2 and Divisible by num2 is {next_num}'
        
result=Next_Num_GreaterThan_AandB_and_Divisible_by_B_func(17,8)
print(result)       
        
    
