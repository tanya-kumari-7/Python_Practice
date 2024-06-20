# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:55:54 2024

@author: user
"""

# =============================================================================
'''
Binary to number
'''
# =============================================================================

dic_list=[]

def binary_to_num_convertor_func(binary):
    dic={}
    num=0
    len_binary=len(str(binary))-1
    for x in str(binary):
        y=(2**len_binary)* int(x)
        num=num+y
        len_binary=len_binary-1
    dic[binary]=num
    dic_list.append(dic)
    print(dic)
    return num

result=binary_to_num_convertor_func(1010)
print(f"result of binary_to_num_convertor_func {result}")
print(dic_list)


