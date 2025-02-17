'''
6. Find Duplicate Number
Given a list of integers containing n+1 integers where each integer is between 1 and n, find the duplicate number.
Example:
Input: [3, 1, 3, 4, 4, 2]
Output: 3,4
''' 
num = [3, 1, 3, 4,4, 2]

def Duplicate_check(num): 
    Output = []
    check =[]
    for x in num:
        if x not in check:
            check.append(x)
        else:
            Output.append(x)

    return Output
              
result = Duplicate_check(num)
print(result)