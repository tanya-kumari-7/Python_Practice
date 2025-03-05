'''
Remove duplicates from a list
'''

num = [12,12,13,14,15,26,28,100,200]

def duplicates_check_func(x): 
    uni = []
    for i in x:
        if i not in uni:
            uni.append(i)
        else:
            continue
    return uni
                 
result = duplicates_check_func(num)
print(result)