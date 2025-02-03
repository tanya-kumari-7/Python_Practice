'''
Fibonacci Series: Generate the first n numbers in 
the Fibonacci sequence.

'''

num = 10
def Fibonacci_func(num):
    num2 = [0,1]
    for x in range(10-2):
        num3 = num2[-1] + num2[-2]
        num2.append(num3)
    return num2

result = Fibonacci_func(num)
print(result)
