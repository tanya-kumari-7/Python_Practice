# Find Second higest number from list

num = [1, 100, 5000, 2002, 300000]

largest = 0 
second =  0

for x in num:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x
        
print(second, largest)
