"""
📌 1️⃣ Reverse a String
Input: "hello" → Output: "olleh"

"""

input_string = 'hello'

def reversed_string_func(x):
    return x[::-1]

result = reversed_string_func(input_string)
print(result)