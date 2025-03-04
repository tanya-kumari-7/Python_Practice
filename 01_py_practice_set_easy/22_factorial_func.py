'''
Find the factorial of a number


'''

num = 10

def factorial_func(x): 
     num2 = 1
     for i in range(1,x+1):
         num2 = num2*i
     return num2
         

result = factorial_func(num)
print(result)