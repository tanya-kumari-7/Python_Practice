'''
Check for Palindrome
Determine if a string reads the same forward and backward.
'''


string = 'Nitin'

def reverse_string_func(string):
    if string.lower() == string[::-1].lower():
        return f'{string} is Palindrome'
    else:
        return f'{string} is Not Palindrome'
        

result = reverse_string_func(string)
print(result)