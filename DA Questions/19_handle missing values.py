''' Q8. How do you handle missing values in a DataFrame? '''

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1, 2,3], 'B': [3, 4,np.NaN]})
df2 = pd.DataFrame({'A': [1, 2,np.NaN], 'C': [5, 6,8]})
df3 = pd.DataFrame({'A': [1, 2,np.NaN,np.NaN], 'C': [5, 6,8,np.NaN]})

# DROP ROWS
df1.dropna(inplace=True)
df1

# Replace value

df2.fillna(0,inplace=True)
