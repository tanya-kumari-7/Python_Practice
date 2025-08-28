"""Reverse a string without using built-in functions."""
string = 'sonam'

def reverse_string_func(x):
    return x[::-1]

result = reverse_string_func(string)
print(result)

"""Check if a string is a palindrome."""
string = 'Nitin'
def palindrome_func(x):
    x1=x.lower()
    if x1[::] == x1[::-1]:
        return f"Yes,{x} is palindrome "
    else:
        return f"No,{x} is not a palindrome "

result = palindrome_func(string)
print(result)





"""Find the first non-repeated character in a string."""

"""Count the frequency of characters in a string."""

"""Find the longest common prefix among strings."""

"""Remove duplicate characters from a string."""
"""Check if two strings are anagrams."""