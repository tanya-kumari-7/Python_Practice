# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:47:47 2024

@author: user
"""

# =============================================================================
'''
Write a Pandas program to count the number of rows and columns 
of a DataFrame.
get_the_count_of_rows_and_columns 
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

# only returns count
df.shape
print('number of rowa',df.shape[0])
print('number of column',df.shape[1])

# coumn name and len counts the numbers
df.axes
print(len(df.axes[0]))
print(len(df.axes[1]))

