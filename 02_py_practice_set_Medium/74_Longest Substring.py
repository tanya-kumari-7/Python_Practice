'''
4. Longest Substring Without Repeating Characters
Find the length of the longest substring without repeating characters.
Example:
Input: "abcabcbbcd"
Output: 3 (substring: "abc")

'''
string = "abcabcbbcdefghij"



def Longest_Substring_func(string): 
    check = []
    output_string = ""
    for x in range(len(string)):
        for i in string[x:]:
            if i not in check:
                check.append(i)
                if len(check) > len(output_string):
                    output_string = "".join(check)
            else: 
                break
        check = []
    return f'lengh of Longest subsrting in the srting "{string}" is {len(output_string)} and longest string is {output_string}'
    
            
result = Longest_Substring_func(string)
print(result)