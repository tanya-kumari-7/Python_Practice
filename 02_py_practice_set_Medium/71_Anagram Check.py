'''
1. Anagram Check
Write a function to check if two strings are anagrams of each other.
Example:
Input: is_anagram("listen", "silent")
Output: True


Key Properties:
The number of letters in both words or phrases must be the same.
The frequency of each letter must match.
Anagrams can be meaningful or nonsensical, but meaningful anagrams are more popular.
'''


def is_anagram_check(is_anagram):
    if len(is_anagram[0]) == len(is_anagram[1]):
        if sorted(is_anagram[0]) == sorted(is_anagram[1]):
            return(f'[{is_anagram}] : TRUE')
            
        else:
            return(f'[{is_anagram}] : FALSE')
    else:
        return(f'[{is_anagram}] : FALSE')
        

result = is_anagram_check(["stressed", "dessers"])
print(result)