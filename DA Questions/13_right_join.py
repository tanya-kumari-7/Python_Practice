''' Q4. What is the difference between merge(), join(), and concat() in Pandas?
A:

merge() – Combines DataFrames based on keys
join() – Combines DataFrames based on the index
concat() – Stacks DataFrames vertically or horizonta 

'''

import pandas as pd
import numpy as np

# join
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [4, 2], 'C': [5, 6]})
 
inner_join = df1.join(df2,on='A',how='inner',lsuffix='left',rsuffix='right')

left_join = df1.join(df2,on='A',how='left',lsuffix='l',rsuffix='r')

right_join = df1.join(df2,on='A',how='right',lsuffix='l',rsuffix='r')