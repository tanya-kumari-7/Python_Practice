'''
2. Dictionary Filtering
Given a dictionary where keys are strings and values are integers, write a function that returns a new dictionary containing only the items where the value is greater than 10.

Example:

input_dict = {'a': 5, 'b': 15, 'c': 25, 'd': 2}
output_dict = {'b': 15, 'c': 25}

'''
input_dict = {'a': 5, 'b': 15, 'c': 25, 'd': 2}


def Dictionary_Filtering_fucn(input_dict):
    output_dict = {}
    for key,value in input_dict.items():
        if value > 10:
            output_dict[key] = value
        else:
            continue
    return output_dict

result = Dictionary_Filtering_fucn(input_dict)
print(result)
            

