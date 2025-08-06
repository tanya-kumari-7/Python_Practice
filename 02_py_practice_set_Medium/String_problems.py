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
def func_vowels_consonants_count(x):
    vowels = []
    consonants = []

    for i in x.lower():
        if i.isalpha():
            if i.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels.append(i)
            else:
                consonants.append(i)
    
    return f"There are {len(vowels)} vowels and {len(consonants)} consonants in '{x}'"

# Example usage
print(func_vowels_consonants_count("nitin"))

## Remove duplicates from a string

string = 'sonanm'
def remove_duplicate_from_string_func(x):
    c = []
    final_str = ''
    for i in x:
        if i not in c:
            c.append(i)
            final_str += "".join(i)
        else:
            continue
    

    return final_str

print(remove_duplicate_from_string_func(string))


### %% Find the most frequent character in a string
  
def func_frequent_character(x):
    di = {}
    for i in x:
        di[i] = di.get(i, 0) + 1
    max_char = max(di, key=di.get)
    
    return max_char,di[max_char]

# Example usage
print(func_frequent_character("sssonam"))  


## Anagram check between two strings
def Anagram_check_func(x,y):
    if len(x) != len(y):
        print(f"{x} and {y} are not a anagram")
        return
    elif len(x) == len(y) and sorted(x) == sorted(y):
        print(f"{x} and {y} are  a anagram")
        return
    else:
        print(f"{x} and {y} are not a anagram")
        return   
print(Anagram_check_func("sonam","snoam"))  



## First non-repeating character

def no_reoeat_char_func(x):
    container = {}
    for i in x:
        if i not in container:
            container[i] = 1
        else:
            container[i] += 1
    for i in x:
        if container[i] == 1:
            return i
 
print(no_reoeat_char_func("ssnoam")) 

## Compress a string (without run-length encoding)


def compress_string_func(x):
    dic_box = {}
    for i  in x :
        if i not in dic_box:
            dic_box[i] = 1
        else :
            dic_box[i] += 1
    result = ''
    for a,b in dic_box.items():
        result += a+str(b)

    return result

print(compress_string_func('sssoonnaammm'))
    

## Compress a string (with run-length encoding)


def compress_string_func(x):
    dic_box = ''
    count = 1
    for i  in range(1,len(x)) :
        if x[i] == x[i-1]:
            count += 1
        else:
            dic_box += x[i-1] + str(count)
            count = 1
    dic_box += x[-1] + str(count)
    return dic_box

print(compress_string_func('sssoonnaammm'))