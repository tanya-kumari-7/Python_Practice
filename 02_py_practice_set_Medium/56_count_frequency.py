
# Write a Python program to count the frequency of elements in a list.
num_list = [1,2,3,4,5,5]
def frequency_func(lst):
    num_frequency_dict = {}
    for x in lst:
        if x not in num_frequency_dict:
            num_frequency_dict[x] = 1
        else:
            num_frequency_dict[x] += 1

    return num_frequency_dict

frequency = frequency_func(num_list)
print(frequency)

