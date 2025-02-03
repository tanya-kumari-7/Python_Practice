'''
Check for Palindrome: Determine if a string reads 
the same forward and backward.
'''

str_ = 'nan'

def Palindrome_func (string):
    if string == string[::-1]:
        return f'{string} is a palindrome string'
    else:
        return f'{string} is not a palindrome string'
        

result = Palindrome_func(str_)
print(result)