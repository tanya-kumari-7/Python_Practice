'''
1. List Manipulation
Given a list of numbers, write a function to return a new list where each element is the square of the original element but only if the original element is even.

nput_list = [1, 2, 3, 4, 5, 6]
output_list = [4, 16, 36]
'''
nput_list = [1, 2, 3, 4, 5, 6]

def square_func(nput_list):
    output_list = []
    for x in nput_list:
        if x % 2 == 0:
            output_list.append(x**2)
    return output_list

result = square_func(nput_list)
print(result)
            

