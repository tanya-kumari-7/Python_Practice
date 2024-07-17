# =============================================================================
'''
Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
'''
# =============================================================================
def Change_Every_Letter_to_the_Next_Letter(string):
    converted_string=''
    for x in string:
        c=chr(ord(x)+1)
        converted_string +=c
    return f"{string} converted string is {converted_string}"
        

        
result=Change_Every_Letter_to_the_Next_Letter('hello')
print(result)