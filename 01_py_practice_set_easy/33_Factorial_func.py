"""
📌 5️⃣ Factorial of a Number
Using loop and recursion both.

"""

input_string = 5

def Factorial_func(num):
    num1= 1
    for x in range(1,num+1):
        num1= num1 * x
    return num1
        
        
  
       
   

result = Factorial_func(input_string)
print(result)


def Factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * Factorial_recursion(num - 1)

result2 = Factorial_recursion(input_string)
print(result2)
