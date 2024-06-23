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
    if num1 > num2:
        Max_num=num1
    else:
        Max_num=num2 
    if num1 > num2:
        Min_num=num2
    else:
        Min_num=num1
        
    next_num=Max_num+1
    for x in range(Max_num,Max_num+10):
        if next_num %  Min_num !=0:
            next_num=next_num+1
    return f'Next Num Greater Than num1 and num2 and Divisible by num2 is {next_num}'
        
result=Next_Num_GreaterThan_AandB_and_Divisible_by_B_func(98,3)
print(result)       
        
    
