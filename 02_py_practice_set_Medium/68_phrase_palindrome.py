'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

string = " "

def phrase_palindrome (price):
    test = []
    for x in string:
        if x.isalnum():
            test.append(x.lower())
            
    if test == test[::-1]:
        return True
    else:
        False

Function_result1 = phrase_palindrome(string)
print(Function_result1)
