'''
Given a list of integers, write a function to return the second 
largest number in the list without using built-in sorting functions.
'''
l=[10,2,3,4,5,6]
max_val = 0
for x in range(len(l)):
    if l[x] > x:
        max_val = l[x]
print(max_val)
