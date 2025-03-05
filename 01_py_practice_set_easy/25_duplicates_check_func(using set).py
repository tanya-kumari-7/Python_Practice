'''
Remove duplicates from a list
'''

num = [12,12,13,14,15,26,28,100,200]

def duplicates_check_func(x): 
      return set(x)
      
             
result = duplicates_check_func(num)
print(result)