'''
98. Anagram Checker
Write a function that takes two strings and checks whether they are anagrams of each other.

Example:

anagram("listen", "silent") -> True
anagram("hello", "world") -> False
'''
input_str = ["hello", "world"]

def anagram_check_func(input_str):
    if len(input_str[0]) == len(input_str[1]):
        if sorted(input_str[0]) == sorted(input_str[1]):
            return True
        else:
            return False
   
result = anagram_check_func(input_str)
print(result)
            

