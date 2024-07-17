# =============================================================================
'''
Write a Pandas program to create a DataFrame from a 
Numpy array and specify the index column and column headers.
''' 
# =============================================================================

import pandas as pd
import numpy as np

dtype = [('Column1','int32'), ('Column2','float32'), ('Column3','float32')]
values = np.zeros(15, dtype=dtype)
index = ['Index'+str(i) for i in range(1, len(values)+1)]

pd.DataFrame(values,index=index)
