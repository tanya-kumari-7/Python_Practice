# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:14:12 2024

@author: user
"""

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def sum_func(self):
        sum_of_nums=self.num1+self.num2
        return sum_of_nums
    
    def sub_func(self):
        sub_of_nums=self.num1-self.num2
        return sub_of_nums
    
    def multiply_func(self):
       multiply_of_nums=self.num1*self.num2
       return multiply_of_nums
    
    def divide_func(self):
       divide_of_nums=round(self.num1/self.num2,0)
       return divide_of_nums
    
Cal_object= calculator(20, 5)

print(Cal_object.sum_func())
print(Cal_object.sub_func())
print(Cal_object.multiply_func())
print(Cal_object.divide_func())
print(Cal_object.num1)
print(Cal_object.num2)