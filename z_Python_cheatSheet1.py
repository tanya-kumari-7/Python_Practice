"""
Python Cheat Sheet
This cheat sheet provides a quick reference for common Python syntax and operations.
"""

# Basic Data Types
"""
- Integers: Whole numbers (e.g., 1, 2, 3)
- Floats: Decimal numbers (e.g., 1.0, 2.5, 3.14)
- Strings: Text (e.g., "Hello, World!")
- Booleans: True or False
"""
# Variables
"""
- Variables are used to store data values.
- In Python, you can create a variable by simply assigning a value to it.
"""
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True  # Boolean

# Basic Operations
"""
# Arithmetic Operations
- Addition: x + y
- Subtraction: x - y
- Multiplication: x * y
- Division: x / y
- Modulus: x % y
"""
# Example Arithmetic Operations
sum_result = x + y
sub_result = x - y
mul_result = x * y
div_result = x / y
mod_result = x % y  

# Print results
print("Sum:", sum_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Modulus:", mod_result)

# Comparison Operations
"""
- Equal to: x == y
- Not equal to: x != y
- Greater than: x > y
- Less than: x < y
- Greater than or equal to: x >= y
- Less than or equal to: x <= y
"""
# Example Comparison Operations
is_equal = (x == y)
is_not_equal = (x != y)
is_greater = (x > y)
is_less = (x < y)
is_greater_equal = (x >= y)
is_less_equal = (x <= y)

# Print comparison results
print("Is Equal:", is_equal)
print("Is Not Equal:", is_not_equal)
print("Is Greater:", is_greater)
print("Is Less:", is_less)
print("Is Greater or Equal:", is_greater_equal)
print("Is Less or Equal:", is_less_equal)

# Logical Operations
"""
- AND: x and y
- OR: x or y
- NOT: not x
"""
# Example Logical Operations
is_true = True
is_false = False
logical_and = is_true and is_false
logical_or = is_true or is_false 
logical_not = not is_true

# Print logical results
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT:", logical_not)

# Control Structures
"""
- If statements: if condition: do something
- For loops: for item in iterable: do something
- While loops: while condition: do something
"""
# Example Control Structures
if is_true:
    print("This is true")

for i in range(5):
    print("Iteration:", i)

while is_false:
    print("This will not print")

# Functions
"""
- Functions are defined using the def keyword.
- They can take parameters and return values.
"""
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
# Example function call
greeting = greet(name)

