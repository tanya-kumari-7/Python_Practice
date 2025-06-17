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

# All about Strings
"""
- Strings are sequences of characters enclosed in quotes.
- You can use single quotes (' ') or double quotes (" ") to define strings. 
"""
# Example Strings
greeting = "Hello, World!"
# String Operations
"""
- Concatenation: str1 + str2
- Repetition: str * n
- Length: len(str)  
- Accessing Characters: str[index]
- Slicing: str[start:end]
"""
# Example String Operations
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
repeated = str1 * 3
length_of_str = len(greeting)
first_char = greeting[0]  # Accessing first character
sliced_str = greeting[0:5]  # Slicing first 5 characters
# Print string results
print("Concatenated String:", concatenated) 
print("Repeated String:", repeated)
print("Length of Greeting:", length_of_str)
print("First Character of Greeting:", first_char)
print("Sliced String:", sliced_str)

# string Formatting
"""
- String formatting allows you to insert variables into strings.
- You can use f-strings (Python 3.6+) or the format() method.
"""
# Example String Formatting
formatted_string = f"{name} is {x} years old."
formatted_string2 = "{} is {} years old.".format(name, x)
# Print formatted strings
print("Formatted String:", formatted_string)
print("Formatted String 2:", formatted_string2)

# string Methods
"""
- Strings have many built-in methods for manipulation.
- Common methods include: 
  - upper(): Converts to uppercase
  - lower(): Converts to lowercase
  - strip(): Removes leading and trailing whitespace
  - split(): Splits a string into a list
  - join(): Joins a list into a string
"""
# Example String Methods
upper_case = greeting.upper()
lower_case = greeting.lower()
stripped_string = greeting.strip()
split_string = greeting.split(", ")
joined_string = " ".join(split_string)
# Print string method results
print("Upper Case:", upper_case)
print("Lower Case:", lower_case)
print("Stripped String:", stripped_string)
print("Split String:", split_string)
print("Joined String:", joined_string)





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

# Print greeting
print(greeting)

# Lists
"""
- Lists are ordered collections of items.
- They can contain mixed data types.
"""
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True]

# Accessing List Elements
"""
- You can access list elements using indexing.
- Indexing starts at 0.
"""
first_element = my_list[0]
second_element = mixed_list[1]

# Print accessed elements
print("First Element:", first_element)
print("Second Element:", second_element)

# Modifying Lists
"""
- Lists are mutable, meaning you can change their content.
"""
my_list[0] = 10
mixed_list.append("new item")

# Print modified lists
print("Modified List:", my_list)
print("Modified Mixed List:", mixed_list)

# Dictionaries
"""
- Dictionaries are collections of key-value pairs.
- They are unordered and mutable.
"""             
my_dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
# Accessing Dictionary Values

name_value = my_dict["name"]
age_value = my_dict["age"]
is_student_value = my_dict["is_student"]

# Print accessed values
print("Name:", name_value)
print("Age:", age_value)
print("Is Student:", is_student_value)

# Modifying Dictionaries
my_dict["age"] = 31  # Update age
my_dict["city"] = "New York"  # Add new key-value pair

# Print modified dictionary
print("Modified Dictionary:", my_dict)

# tuples
"""
- Tuples are ordered collections of items, similar to lists.        
- They are immutable, meaning their content cannot be changed after creation.
"""
my_tuple = (1, 2, 3, "four", True)

# Accessing Tuple Elements
first_tuple_element = my_tuple[0]

# Print accessed tuple element
print("First Tuple Element:", first_tuple_element)

# Sets
"""
- Sets are unordered collections of unique items.
- They are mutable and do not allow duplicate values.
"""

my_set = {1, 2, 3, 4, 5}
# Adding and Removing Elements from a Set
my_set.add(6)  # Add an element
my_set.remove(2)  # Remove an element

# Print modified set
print("Modified Set:", my_set)

# lambda Functions
"""
- Lambda functions are small anonymous functions defined using the lambda keyword.
- They can take any number of arguments but can only have one expression.   

"""
add = lambda x, y: x + y
# Example lambda function call

result = add(5, 3)
# Print lambda function result
print("Lambda Function Result:", result)    

# List Comprehensions
"""
- List comprehensions provide a concise way to create lists.
- They consist of brackets containing an expression followed by a for clause.
"""
squared_numbers = [x**2 for x in range(10)]
# Print list comprehension result
print("Squared Numbers:", squared_numbers)

# Exception Handling
"""
- Exception handling is done using try and except blocks.
- It allows you to handle errors gracefully without crashing the program.
"""
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block always executes, regardless of an error.")

