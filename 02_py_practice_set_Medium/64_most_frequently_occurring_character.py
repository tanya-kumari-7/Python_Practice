'''
Write a function that takes a string as input and returns the most 
frequently occurring character. Ignore spaces and punctuation.
'''
def check(string):
    dict_ ={}
    for x in string:
        if x not in dict_:
            dict_[x] = 1
        else:
            dict_[x] += 1
    return(max(dict_.items()))

result=check('stt')
print(result)