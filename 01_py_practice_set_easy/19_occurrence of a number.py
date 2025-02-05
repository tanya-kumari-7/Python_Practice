# find the time of occurrence of a number in a list


num = [1,2,1,2,2,2,2]
result_dict = {}
check = []

for x in num:
    if x not in check:
        check.append(x)
        result_dict[x] = 1
    else:
        result_dict[x] += 1
        
print(result_dict)
        
        