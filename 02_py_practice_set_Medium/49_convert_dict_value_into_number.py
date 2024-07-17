# =============================================================================
'''
You prepare a list to send to the insurance company. 
As you finish, you notice you misformatted it. Given a dictionary 
with at least one key/value pair, convert all the values to 
numbers.

Examples
'''
# =============================================================================


def convert_dict_value_into_number(dic):
    for key,value in dic.items():
        dic[key]=int(dic[key])
    return dic

result=convert_dict_value_into_number({ "piano": "200", "tv": "300", "stereo": "400" })
print(result)
