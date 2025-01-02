'''
# Find the largest and smallest numbers in a list.
num_list = [10,20,30,40,50,1000]
def find_min_max_fucn(lst):
    return min(lst),max(lst)
            

find_min_max = find_min_max_fucn(num_list)
print(find_min_max)
'''


# Find the largest and smallest numbers in a list.
num_list = [10,20,30,40,50,1000]
def find_min_max_fucn(lst):
    min_ = lst[0]
    max_ = lst[0]
    for x in lst:
        if x < min_:
            min_ = x
        if x > max_:
            max_ = x
    return f'{min_} is a min number in the list {max_} is a max number in a this list'
            
        
find_min_max = find_min_max_fucn(num_list)
print(find_min_max)


