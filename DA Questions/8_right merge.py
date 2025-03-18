''' Q4. What is the difference between merge(), join(), and concat() in Pandas?
A:

merge() – Combines DataFrames based on keys
join() – Combines DataFrames based on the index
concat() – Stacks DataFrames vertically or horizonta 

'''

import pandas as pd
import numpy as np

# merge
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [4, 2], 'C': [5, 6]})
                                       
mergedf = df1.merge(df2, on= 'A', how= 'inner')                                      
mergedf
mergedf2 = pd.merge(df1,df2,on='A',how = 'inner')
mergedf2

mergedf = df1.merge(df2, on= 'A', how= 'left')                                      
mergedf
mergedf2 = pd.merge(df1,df2,on='A',how = 'left')
mergedf2

mergedf = df1.merge(df2, on= 'A', how= 'right')                                      
mergedf
mergedf2 = pd.merge(df1,df2,on='A',how = 'right')
mergedf2