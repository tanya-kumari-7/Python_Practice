str_1 = 'pwwkew'
str_2= []
str_3 = []
str_4 =[]
 
for x in str_1:
    if x not in str_2:
        str_2.append(x)
    else:
        continue
    str_3 = ''.join(str_2)
str_4.append(str_3)
        
print(str_4)
    