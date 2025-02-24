'''
5. Fibonacci Sequence
Write a function that returns the first n numbers of the Fibonacci sequence.

Example:

fibonacci(6)
output = [0, 1, 1, 2, 3, 5]

'''
num = 6

def fibonacci_func(num):
    output=[0,1]
    for x in range(2,num):
        output.append(output[-1]+output[-2])
    return  output
        
result = fibonacci_func(num)
print(result)
            

