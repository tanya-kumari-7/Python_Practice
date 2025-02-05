# How would you retrieve all rows where column contain 
# duplicate, but only showing the duplicate value. 

num = [1,2,3,4,5,6,7,7,8,10,20]
duplicate_record =[]
unique_record = []

for x in num:
    if x not in unique_record:
        unique_record.append(x)
    else:
        duplicate_record.append(x)
        
print(f'Duplicate list is {duplicate_record}')
print(f'unique list is {unique_record}')