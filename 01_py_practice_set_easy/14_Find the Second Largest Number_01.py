'''
Find the Second Largest Number
'''

def Second_Largest_Number_func(list_1):
    list_1 = list(set(list_1))  # Remove duplicates using set
    list_1.sort()  # Sort the list
    return list_1[-2]  # The second last element is the second largest

a = [10, 2, 1, 3000, 40000]
result = Second_Largest_Number_func(a)
print(result)
