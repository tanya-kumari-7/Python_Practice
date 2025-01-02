def Fibonacci_func(n):
    Fibonacci_list = [0, 1]
    num = 1
    while num +Fibonacci_list[-2] <= n:  # Include numbers that are less than or equal to n
        new_num = Fibonacci_list[-1] + Fibonacci_list[-2]
        Fibonacci_list.append(new_num)
        num = new_num
    return Fibonacci_list

output = Fibonacci_func(10)
print(output)
