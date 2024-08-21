# =============================================================================
'''
Write a Pandas program to split the following dataframe into groups based on first 
column and set other column values into a list of values.

'''
# =============================================================================
import pandas as pd

df = pd.DataFrame( {'X' : [10, 10, 10, 20, 30, 30, 10], 
                    'Y' : [10, 15, 11, 20, 21, 12, 14], 
                    'Z' : [22, 20, 18, 20, 13, 10, 0]})

result=df.groupby('X').agg(list)

