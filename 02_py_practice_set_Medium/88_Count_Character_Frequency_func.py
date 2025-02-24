'''
9. Count Character Frequency
Write a function that takes a string and returns a dictionary with the count of each character.

Example:

input_str = "banana"
output = {'b': 1, 'a': 3, 'n': 2}

'''
input_str = "banana"

def Count_Character_Frequency_func(input_str):
    dict_ = {}
    for x in input_str:
        if x not in dict_:
            dict_[x] = 1
        else:
            dict_[x] += 1
    return dict_
   
result = Count_Character_Frequency_func(input_str)
print(result)
            

