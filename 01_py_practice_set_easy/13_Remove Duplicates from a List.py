'''
Find the Second Largest Number
'''
a = [10,2,1,3000,400]

def Second_Largest_Number_func(list_1):
    largest = []
    check = 0
    for x in range(len(a)):
        if a[x] > check:
            check = a[x]
            largest.append(check)
    return largest[::-1]
        
result = Second_Largest_Number_func(a)
print(result)

