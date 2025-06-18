"""
📌 4️⃣ Fibonacci Series
Print first N Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, ...

"""

input_string = 15

def Fibonacci_func(num):
    result = [0,1]
    for x in range(num-2):
        num2 = result[-1] + result[-2]
        result.append(num2)
    return result
  
       
   

result = Fibonacci_func(input_string)
print(result)