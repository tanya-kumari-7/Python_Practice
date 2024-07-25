# =============================================================================
'''
Write a Pandas program to convert DataFrame column type from 
string to datetime.
''' 
# =============================================================================

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df=pd.DataFrame(exam_data,index=labels)
print(df)

df['datetime'] = ['3/11/2000', '3/12/2000', '3/13/2000', '3/14/2008', '3/12/2000',
                  '3/13/2000', '3/15/2002', '3/12/2003', '3/9/2000', '3/16/2001']

df['datetime'] =pd.to_datetime(df['datetime'])
