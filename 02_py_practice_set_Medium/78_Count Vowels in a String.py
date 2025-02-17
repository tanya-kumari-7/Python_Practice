'''
8. Count Vowels in a String
Write a function that counts the number of vowels in a string.
Example:
Input: "hello world"
Output: 3

''' 
string = "hello world"

output = 0
for x in string:
    if x in 'aeiou':
        output += 1
        
print(output)
