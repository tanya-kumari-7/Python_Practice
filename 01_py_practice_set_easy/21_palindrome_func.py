'''
Check if a string is a palindrome


'''

string = 'nitin'

def palindrome_func(x): 
     if x == x[::-1]:
         return f'Yes, {x} is a Palindrome string'
     else:
         return f'No, {x} is not a Palindrome string'
         

result = palindrome_func(string)
print(result)