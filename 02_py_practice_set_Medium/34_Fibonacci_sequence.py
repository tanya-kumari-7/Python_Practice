# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:12:56 2024

@author: user
"""

# =============================================================================
# Create a Fibonacci sequence
# =============================================================================

''' Method one '''
def Fibonacci_sequence(num):
    Fibonacci_list=[0,1]
    for x in range(1,num-1):
        next_num=Fibonacci_list[-1]+Fibonacci_list[-2]
        Fibonacci_list.append(next_num)
    return Fibonacci_list

result = Fibonacci_sequence(15)
print(result)

'''Method two'''

def Fibonacci_sequence2(num):
    Fibonacci_list2=[]
    a=0
    b=1
    for x in range(num):
        if len(Fibonacci_list2)==0:
            Fibonacci_list2.append(a)
        else:
            c=a+b
            b=a
            a=c
            Fibonacci_list2.append(c)
    
    return Fibonacci_list2

result = Fibonacci_sequence2(10)
print(result)


        
    
  
    
    
