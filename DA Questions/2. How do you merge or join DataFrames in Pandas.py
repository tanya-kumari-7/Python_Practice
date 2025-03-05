'''
2. How do you merge or join DataFrames in Pandas?

'''

import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4],
                    'Score': [85, 90, 95]})


df = df1.merge(df2,on="ID",how='inner')
print(df)

df_ = pd.merge(df1, df2,on="ID",how = "inner")
print(df_)