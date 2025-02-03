'''
Find the Factorial: Compute the factorial of a given 
number using recursion.
'''

num = 10
def Factorial_func(num):
    num2 = 1
    for x in range(1,(num+1)):
        num2 = num2 * x
    return num2

result = Factorial_func(num)
print(result)

#####################################
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = 10
result = factorial_recursive(num)
print(result)
