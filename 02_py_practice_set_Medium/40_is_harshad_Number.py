# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:57:19 2024

@author: user
"""

# =============================================================================
'''
A number is said to be Harshad if it's exactly divisible by 
the sum of its digits. Create a function that determines 
whether a number is a Harshad or not.
'''
# =============================================================================

# Harshad_Number

def is_harshad_Number(num):
    sum_=0
    for x in str(num):
        sum_ += int(x)
    if num % sum_ == 0:
        return f"{num} is harshad as it's exactly divisible by it's sum {sum_}"
    return f"{num} is not harshad as it's not divisible by it's sum {sum_}"

result=is_harshad_Number(171)
print(result)
