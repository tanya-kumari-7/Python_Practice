'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

string = "pwwkew"
max_length = 0
longest_substr = ""
   
for i in range(len(string)):
    check = []
    for x in string[i:]:
        if x not in check:
            check.append(x)
        else:
            break
    if len(check) > max_length:
        max_length = len(check)
        longest_substr = "".join(check) 
        
print(longest_substr,max_length)
   


    
    
    
        
        


# def phrase_palindrome (price):
#     test = []
#     for x in string:
#         if x.isalnum():
#             test.append(x.lower())
            
#     if test == test[::-1]:
#         return True
#     else:
#         False

# Function_result1 = phrase_palindrome(string)
# print(Function_result1)
