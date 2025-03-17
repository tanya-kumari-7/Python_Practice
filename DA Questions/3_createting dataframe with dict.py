''' Q1. How do you create a DataFrame from a dictionary? '''

import pandas as pd

data = {
        'Name':['sonam','monam','tonam','ponam','lonam'],
        'age':[10,15,20,25,30]
        }

df = pd.DataFrame(data)
print(type(df))
print(data)