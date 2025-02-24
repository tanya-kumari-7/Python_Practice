'''
. List Comprehension Challenge
Given a list of numbers, generate a new list that contains only the numbers that are divisible by both 3 and 5.

Example:

input_list = [10, 15, 20, 30, 45, 60, 75]
output = [15, 30, 45, 60, 75]

'''
input_list = [10, 15, 20, 30, 45, 60, 75]

def List_Comprehension_Challenge(input_list):
    output = []
    for x in input_list:
        if x % 3 == 0 and x % 5 == 0:
            output.append(x)
        else:
            continue
    return output
   
result = List_Comprehension_Challenge(input_list)
print(result)
            

