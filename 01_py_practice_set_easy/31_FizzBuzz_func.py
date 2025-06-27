"""
📌 3️⃣ FizzBuzz
Print numbers 1 to N:
    If divisible by 3 → "Fizz"
    If divisible by 5 → "Buzz"
    If both → "FizzBuzz"

"""

input_string = 10

def FizzBuzz_func(num):
    for x in range(1,num+1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        if x % 3 == 0 :
            print("Fizz")
        if x % 5 == 0:
            print("Buzz")
        else:
            print(x)
   

result = FizzBuzz_func(input_string)
print(result)