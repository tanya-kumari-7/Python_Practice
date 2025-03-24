''' Q9. How can you identify and remove duplicate rows in a DataFrame?'''

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1, 2,1], 'B': [3, 4,3]})

df1.duplicated()
df1.drop_duplicates(inplace=True)




