# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:57:14 2024

@author: user
"""

# =============================================================================
'''
Create a function that takes a string and returns the sum of 
vowels, where some vowels are considered numbers.

Vowel	Number
A	4
E	3
I	1
O	0
U	0

'''
# =============================================================================


def Sum_of_v0w3ls_check(statement):
    vowels_dic={'a':4,'e':3,'i':1,'o':0 ,'u':0}
    sum_of_vowel=0
    for x in statement:
        for key,value in vowels_dic.items():
            if x.lower() == key.lower():
                sum_of_vowel += value
    
    return f'sum of vowels in the statement is {sum_of_vowel}'

result=Sum_of_v0w3ls_check("I love edabit!")
print(result)
