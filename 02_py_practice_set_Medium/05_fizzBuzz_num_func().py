# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:47:31 2024

@author: user
"""

# =============================================================================
'''
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
'''
# =============================================================================


def fizzBuzz_num_func(n):
    if n % 3 ==0:
        return 'fizz'
    elif n% 5 == 0:
        return 'buzz'
    elif n% 3==0 and n % 5 == 0:
        return 'fizzbuzz'
    else:
       return str(n) 
   
result = fizzBuzz_num_func(15)
print(f'result of fizzBuzz_num_func is {result}')
