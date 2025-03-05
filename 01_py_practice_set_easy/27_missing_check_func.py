'''
find missing num from a list
'''

num = [12,12,13,14,15,26,28,100,200]

def missing_check_func(x): 
    uni = []
    for i in range(min(x),max(x)):
        if i not in x:
            uni.append(i)
        else:
            continue
    return uni
                 
result = missing_check_func(num)
print(result)