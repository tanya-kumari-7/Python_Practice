# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:46:01 2024

@author: user
"""

# =============================================================================
# Create a function that takes two number strings and returns 
# their sum as a string.
# add("111", "111") ➞ "222"
# add("10", "80") ➞ "90"
# add("", "20") ➞ "Invalid Operation"
# =============================================================================

def sum_of_num1_and_num2_which_is_in_str_func(num1,num2):
    try:
        sum_of_num=int(num1)+int(num2)
        return f'sum of num1 and num2 is {str(sum_of_num)}'
    except Exception as e:
        print(f'Invalid Operation error is {e}')

result=sum_of_num1_and_num2_which_is_in_str_func('111','111')
print(result)