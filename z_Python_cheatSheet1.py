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

# Like Operator [''' Using in (like SQL %word%) ''']
text = "I love Python programming"

print("Python" in text)   # True  (like SQL: WHERE text LIKE '%Python%')
print("Java" in text)     # False




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

# all about Lists

"""
- Lists are ordered collections of items.
- They can contain mixed data types and are defined using square brackets [].

"""
# Example Lists
my_list = [1, 2, 3, "four", True]
# List Operations
"""
- Accessing Elements: list[index]
- Slicing: list[start:end]
- Adding Elements: list.append(item)
- Removing Elements: list.remove(item)
- Length: len(list)
"""

# Example List Operations
first_item = my_list[0]  # Accessing first element
second_item = my_list[1:3]  # Slicing first two elements
my_list.append("new item")  # Adding an item
my_list.remove(2)  # Removing an item
list_length = len(my_list)  # Getting the length of the list
# Print list results
print("First Item:", first_item)
print("Second Item:", second_item)
print("Modified List:", my_list)
print("List Length:", list_length)

# All about Dictionaries
"""
- Dictionaries are collections of key-value pairs.
- They are unordered and mutable, defined using curly braces {}.
"""
# Example Dictionaries
my_dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
# Dictionary Operations

"""
- Accessing Values: dict[key]
- Adding/Updating Values: dict[key] = value
- Removing Values: del dict[key]
- Keys: dict.keys()
- Values: dict.values()
"""
# Example Dictionary Operations
name_value = my_dict["name"]  # Accessing value by key
age_value = my_dict["age"]  # Accessing value by key
is_student_value = my_dict["is_student"]  # Accessing value by key
# Adding a new key-value pair
my_dict["city"] = "New York"  # Adding a new key-value pair
# Updating an existing key-value pair
my_dict["age"] = 31  # Updating age
# Removing a key-value pair
del my_dict["is_student"]  # Removing is_student key
# Print dictionary results
print("Name:", name_value)
print("Age:", age_value)
print("Is Student:", is_student_value)
print("Modified Dictionary:", my_dict)


# All about Tuples
"""
- Tuples are ordered collections of items, similar to lists.
- They are immutable, meaning their content cannot be changed after creation.
"""
# Example Tuples
my_tuple = (1, 2, 3, "four", True)
# Tuple Operations
"""
- Accessing Elements: tuple[index]
- Slicing: tuple[start:end]
- Length: len(tuple)
"""
# Example Tuple Operations
first_tuple_element = my_tuple[0]  # Accessing first element
second_tuple_elements = my_tuple[1:3]  # Slicing first two elements
tuple_length = len(my_tuple)  # Getting the length of the tuple
# Print tuple results
print("First Tuple Element:", first_tuple_element)
print("Second Tuple Elements:", second_tuple_elements)
print("Tuple Length:", tuple_length)

# All about Sets
"""
- Sets are unordered collections of unique items.
- They are mutable and defined using curly braces {}.
"""
# Example Sets
my_set = {1, 2, 3, 4, 5}
# Set Operations

"""
- Adding Elements: set.add(item)
- Removing Elements: set.remove(item)
- Checking Membership: item in set
- Length: len(set)
"""
# Example Set Operations
my_set.add(6)  # Adding an element
my_set.remove(2)  # Removing an element

# Checking membership
is_in_set = 3 in my_set  # Checking if 3 is in the set
set_length = len(my_set)  # Getting the length of the set
# Print set results
print("Modified Set:", my_set)
print("Is 3 in Set:", is_in_set)






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


# File I/O

"""
- File I/O allows you to read from and write to files.
- You can use the open() function to open a file and read or write data.
""" 
# Example File I/O
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")
# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
# Print file content
print("File Content:")
print(content)

# Modules and Packages
"""
- Modules are files containing Python code that can be imported into other Python scripts.
- Packages are collections of modules organized in directories.
"""
# Example of importing a module
import math
# Using a function from the math module
sqrt_result = math.sqrt(16)

# Print square root result
print("Square Root of 16:", sqrt_result)

# Conclusion
""" 
This cheat sheet provides a quick overview of Python syntax and operations.
For more detailed information, refer to the official Python documentation or other resources.
"""
# advanced python concepts and cheatsheet

"""
- Python has many advanced features and concepts that can enhance your programming skills.  
- This section covers some of these advanced concepts, including decorators, generators, context managers, and more.
"""
# Decorators
"""
- Decorators are functions that modify the behavior of other functions or methods.
- They are often used to add functionality to existing code without modifying it.
"""
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    """Function to display a message."""
    print("Display function executed.")
# Example decorator usage
display()  # Call the decorated function
# Generators
"""
- Generators are functions that return an iterator using the yield keyword.
- They allow you to iterate over a sequence of values without storing the entire sequence in memory.
"""
def generator_function():
    yield 1
    yield 2
    yield 3


# Example generator usage
gen = generator_function()
for value in gen:
    print("Generator Value:", value)
# Context Managers
"""
- Context managers are used to manage resources, typically with the with statement.
- They ensure that resources are properly acquired and released, even in the presence of errors.
"""
class ContextManagerExample:
    def __enter__(self):
        print("Entering context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context.")
        if exc_type:
            print(f"An error occurred: {exc_value}")
# Example context manager usage
with ContextManagerExample() as cm:
    print("Inside context.")
    # Uncomment the next line to see error handling in action
    # raise ValueError("An example error.")
print("Outside context.")
# List Comprehensions with Conditionals
"""

- List comprehensions can include conditionals to filter items.
"""
filtered_numbers = [x for x in range(10) if x % 2 == 0]
# Print filtered list
print("Filtered Even Numbers:", filtered_numbers)
