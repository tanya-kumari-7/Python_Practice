'''✅ String Problems '''

## Reverse a string

string = 'sonam'

def func_reverse_string(x):
    return x[::-1]

func_call = func_reverse_string(string)
print(func_call)

## Check if a string is a palindrome   

def func_palindrome_check(x):
    if x == x[::-1]:
        return f'{x}: is a palindrome'
    else:
        return f'{x}: is not a palindrome'
    
func_call = func_palindrome_check(string)
print(func_call)


## Count vowels/consonants

def func_vowels_consonants_count (x):
    vowels = []
    consonants = []

    for i in x :
        if i in ('a','e','i','o','u'):
            vowels.append(i)
        
            


    
    