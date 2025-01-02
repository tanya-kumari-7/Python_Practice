
# Check if a string is a palindrome.
name_list = ['nitin','sonam','gog','pop','gaurav']
def palindrome_func(lst):
    result =[]
    for x in lst:
        if x == x[::-1]:
            result.append(f'{x} is a palindrome')
        else:
            result.append(f'{x} is not a palindrome')
    return result
            
            

palindrome = palindrome_func(name_list)
print(palindrome)

