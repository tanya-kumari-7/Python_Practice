'''
10. Prime Number Check
Write a function that checks if a given number is prime.

Example:

is_prime(7) -> True
is_prime(10) -> False

'''
is_prime = 101

def prine_num_check(is_prime):
    for x in range(2,is_prime):
        if is_prime % x == 0:
            return False
        else:
            return True
   
result = prine_num_check(is_prime)
print(result)
            

