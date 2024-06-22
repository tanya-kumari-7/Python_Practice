# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:32:02 2024

@author: user
"""

num_of_list=[2,1,3,4,5,6,78,9,10,2,3,4,7]

def sum_of_odd_and_even_num_calculator(n):
    sum_of_even_and_odd_from_list=[]
    even_dic={}
    odd_dic={}
    sum_of_even=0
    sum_of_odd=0
    for x in n:
        if x % 2 ==0:
            sum_of_even +=x
        else:
            sum_of_odd +=x
    even_dic['even']=sum_of_even
    odd_dic['odd']=sum_of_odd
    sum_of_even_and_odd_from_list.append(even_dic)
    sum_of_even_and_odd_from_list.append(odd_dic)
    return sum_of_even_and_odd_from_list
    
result=sum_of_odd_and_even_num_calculator(num_of_list)
print(f'{result}')
    
    
    