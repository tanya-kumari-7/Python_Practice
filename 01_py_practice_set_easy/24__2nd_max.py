'''
Find the second largest element in list
'''

num = [12,13,14,15,26,28,100,200]
_2nd_max = 0
max_num = 0
for x in num:
    if x > max_num:
        _2nd_max = max_num
        max_num = x
        
print(_2nd_max)


# def prime_check_func(x): 
#      for i in range (2,x):
#          if x % i == 0:
#              return f'No, Num {x} is not a prime number'
#      return f'Yes, Num {x} is  a prime number'
      
             
# result = prime_check_func(num)
# print(result)