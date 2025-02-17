'''
2. Find the Missing Number
Given a list of integers from 1 to n with one number missing, find the missing number.
Example:
Input: [1, 2, 4, 5]
Output: 3

'''
num = [1, 2, 4, 5,10]

def Missing_Number_func(num):
    output = []
    max_num = max(num)
    min_num = min(num)
    for x in range(min_num,max_num):
        if x not in num:
            output.append(x)
        else:
            continue
    return output
        
result = Missing_Number_func(num)
print(result)