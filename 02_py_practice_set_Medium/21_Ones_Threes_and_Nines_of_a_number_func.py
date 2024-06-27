# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:42:12 2024

@author: user
"""

# =============================================================================
# Given an int, figure out how many ones, threes and nines you could 
# fit into the number. You must create a class. You will make variables
#  (self.ones, self.threes, self.nines) to do this.
# =============================================================================

class Ones_Threes_and_Nines:
    # def __init__(self):
    #     self.ones=ones
    #     self.threes=threes
    #     self.nines=nines
        
    def ones(self,num):
        return f'{num//1} times 1 can be fit with {num}'
    def threes(self,num):
        return f'{num//3} times 3 can be fit with {num}'
    def nines(self,num):
        return f'{num//9} times 9 can be fit with {num}'

Ones_Threes_and_Nines_object=Ones_Threes_and_Nines()
print(Ones_Threes_and_Nines_object.ones(50))
print(Ones_Threes_and_Nines_object.threes(50))
print(Ones_Threes_and_Nines_object.nines(50))