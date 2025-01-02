
# factorial of a number

def factorial(n):
    factorial_num = 1
    for x in range(1,n+1):
        if n == 1 or n==0:
            return n
        factorial_num = factorial_num * x
    return factorial_num

factorial_of = factorial(10)
print(factorial_of)
        