'''
5. Two Sum Problem
Given a list of numbers and a target sum, return the indices of the two numbers that add up to the target.
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
''' 
num = [2, 7, 11, 15]
target = 26

def two_sum_problem(num,target): 
    Output = []
    for x in range(0,len(num)):
        for i in range(x+1,len(num)):
            if num[x] + num[i] == target:
                Output.append(x)
                Output.append(x+1)

    return Output
              
result = two_sum_problem(num,target)
print(result)