# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:57:34 2024

@author: user
"""

# =============================================================================
'''
Check_If_Lines_Are_Parallel
Given two lines, determine whether or not they are parallel.
Lines are represented by a list [a, b, c], which corresponds to 
the line ax+by=c.

'''
# =============================================================================
line1=[1, 2, 3]
line2=[1, 2, 4]

def are_lines_parallel(line1,line2):
    a1,b1,c1=line1
    a2,b2,c2=line2
    if a1*b2 == a2*b1:
        return f'lines are parallel'
    else:
        return f'lines are not parallel'
    
result=are_lines_parallel(line1, line2)
print(result)
