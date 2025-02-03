'''
Check for Prime Number: Determine if a number is prime.
'''

num = 1
def Prime_func(num):
    if num < 2:
        f"{num} is a prime number"
        
    for x in range(2,(num)):
        if num % x == 0:
            return f"{num} is not a prime number"
            break
    return f"{num} is a prime number"

result = Prime_func(num)
print(result)
