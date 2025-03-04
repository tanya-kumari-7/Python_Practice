'''
Check if a number is prime
'''

num = 3

def prime_check_func(x): 
     for i in range (2,x):
         if x % i == 0:
             return f'No, Num {x} is not a prime number'
     return f'Yes, Num {x} is  a prime number'
      
             
result = prime_check_func(num)
print(result)