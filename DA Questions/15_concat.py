''' Q4. What is the difference between merge(), join(), and concat() in Pandas?
A:

merge() – Combines DataFrames based on keys
join() – Combines DataFrames based on the index
concat() – Stacks DataFrames vertically or horizonta 

'''

import pandas as pd
import numpy as np

# concat
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [4, 2], 'C': [5, 6]})
 
concat = pd.concat([df1,df2])
