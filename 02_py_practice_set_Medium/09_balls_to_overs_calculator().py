# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:10:01 2024

@author: user
"""

# =============================================================================
'''Cricket Balls to Overs!
In cricket, an over consists of six deliveries a bowler bowls 
from one end. Create a function that takes the number of balls 
bowled by a bowler and calculates the number of overs and balls 
bowled by him/her. Return the value as a float, in the format 
overs.balls.'''
# =============================================================================

def balls_to_overs_calculator(number_of_balls):
    overs=round(number_of_balls/6,1)
    return overs

result=balls_to_overs_calculator(2700)
print(f'over is {result}')
    