# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:47:47 2024

@author: user
"""

# =============================================================================
'''
Write a Pandas program to append a new row 'k' to data frame
with given values for each column. Now delete the new row and 
return the original
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

# adding new row
df.loc['k']=['Suresh',15.5,1,'yes']
# deleteing the new created row
df=df.drop('k')
df
