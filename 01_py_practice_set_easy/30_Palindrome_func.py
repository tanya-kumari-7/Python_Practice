"""
📌 2️⃣ Check for Palindrome

Input: "madam" → Palindrome
Input: "hello" → Not Palindrome"

"""

input_string = 'hello'

def Palindrome_func(x):
    if x == x[::-1]:
        return f'{x} is a Palindrome'
    else:
        return f'{x} is not a Palindrome'

result = Palindrome_func(input_string)
print(result)