list_1 = [1,2,3,4,5,6,6,7,8,8]

dup_list = []
store = []
for x in list_1:
    if x not in store:
        store.append(x)
    else:
        dup_list.append(x)

print(dup_list)
