# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:22:33 2024

@author: user
"""

# =============================================================================
# Stupid Addition
# Create a function that takes two parameters and, if both parameters 
# are strings, add them as if they were integers or if the two parameters
#  are integers, concatenate them.
# =============================================================================

def Stupid_Addition_func(num1,num2):
    if type(num1) == int and type(num2)==int :
        return str(num1)+str(num2)
    elif  type(num1) == str and type(num2)==str :
        return int(num1)+int(num2)
    elif ( type(num1) ==str and type(num2)==int ) or (type(num1) ==int and type(num2)==str):
        return 'None'

result=Stupid_Addition_func('1',2)
print(result)