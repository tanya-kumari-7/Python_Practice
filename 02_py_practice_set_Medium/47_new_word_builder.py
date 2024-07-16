# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:47:21 2024

@author: user
"""
# =============================================================================
'''
Create a function that builds a word from the scrambled letters 
contained in the first list. Use the second list to establish 
each position of the letters in the first list. Return a string 
from the unscrambled letters (that made-up the word).
'''
# =============================================================================

def new_word_builder(list1,list2):
    word=''
    for x in list2:
        word= f"{word}{list1[x]}"
    return word
    
result=new_word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2])
print(result)
        
        
            
