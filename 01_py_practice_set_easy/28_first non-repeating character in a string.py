'''
Find the first non-repeating character in a string
'''


text = "racecar"

def func(x): 
    for a in range(len(x)):
        if x[a] not in x[:a]+x[a+1:]:
            uni = x[a]
            
            return x[a]
                 
result = func(text)
print(result)