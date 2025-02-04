# How would you find missing number i a list

num = [1,2,3,4,5,6,8,10,20]
missing_num =[]

for x in range(min(num),max(num)):
    if x not in num:
        missing_num.append(x)
        
print(missing_num)
    