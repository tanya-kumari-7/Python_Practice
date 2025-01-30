def str_check(str_1):
    str_2= []
    str_4 =[]
    i = 0
    while i < len(str_1):
        for x in str_1[i:]:
            if x not in str_2:
                str_2.append(x)
            else:
                break
        str_4.append(''.join(str_2))
        str_2 = []
        i += 1    
    len_check = 0
    sub_str = []
    for x in str_4:
        if len(x) > len_check:
            len_check = len(x)
            sub_str = x
    return(len_check,sub_str)

result = str_check('pwwkew')
print(result)
    
            
            