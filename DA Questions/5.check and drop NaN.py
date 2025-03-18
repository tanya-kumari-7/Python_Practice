''' Q3. How do you drop rows with missing values in a DataFram'''

import pandas as pd
import numpy as np

data = {
        'Name':['sonam','monam','tonam','ponam','lonam'],
        'age':[10,15,20,25,30],
        'page':[10,20,30,40, np.NaN]
        }

df = pd.DataFrame(data)
print(df)

df.isnull().sum()
df.dropna(inplace= True)
df
