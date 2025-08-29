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
string = 'sonam'

def first_non_repeated_character(string):
    for ch in string:
        if string.count(ch) == 1:
            return f"{ch} is the first non-repeated character"
    return "No non-repeated character found"

result = first_non_repeated_character(string)
print(result)

"""Count the frequency of characters in a string."""
string = 'nitin'

dic = {}
for x in string:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
print(dic)

"""Find the longest common prefix among strings."""
string = ["interspecies", "interstellar", "interstate"]

l1=[]
l2=[]
l3=[]




for x in string:


"""Remove duplicate characters from a string."""
string = 'sonam'
"""Check if two strings are anagrams."""
string = 'sonam'