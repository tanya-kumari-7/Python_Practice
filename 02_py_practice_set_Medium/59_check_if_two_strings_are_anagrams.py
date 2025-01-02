# Implement a function to check if two strings are anagrams.

lis = ['listen','silent']

def anagrams_func(lst):
    print(sorted(lst[0]))
    print(sorted(lst[1]))
    if sorted(lst[0]) == sorted(lst[1]):
        return f'{lst} is a anagrams'
    else:
        return f'{lst} is not a anagrams'

output = anagrams_func(lis)
print(output)