'''
Remove Duplicates from a List
'''
a = [1,2,2,3,4,'sonam','tanya','tanya']

def Remove_Duplicates_func(list_1):
    unique_list=[]
    dupli_list = []
    for x in list_1:
        if x not in unique_list:
            unique_list.append(x)
        else:
            dupli_list.append(x)
    return f'{unique_list} &  {len(dupli_list)} is a duplicate count in a list'
   
            
result = Remove_Duplicates_func(a)
print(result)
