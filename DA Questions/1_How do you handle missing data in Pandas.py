'''
1. How do you handle missing data in Pandas?

'''

import pandas as pd

df = pd.DataFrame({'A': [1, None, 3, 4],
                   'B': [None, 2, 3, 4]})


#...............checking column wise null count
df.isnull().sum()

#...............fill NA values
df = df.fillna(0).astype(df.dtypes)
df


