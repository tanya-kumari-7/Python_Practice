'''
3. Reverse a  List


'''
num = [1, 2, 4, 5,10]


def reverse_list_func(num):
    sorted_list = sorted(num)
    return f'reversed list is {sorted_list[::-1]}'
    
        
result = reverse_list_func(num)
print(result)