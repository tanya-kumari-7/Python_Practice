# =============================================================================
'''
Write a Pandas program to reset index in a given DataFrame.
''' 
# =============================================================================
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# df=pd.DataFrame(exam_data,index=labels)
new_index=[1,2,3,4,5,6,7,8,9,10]
df=pd.DataFrame(exam_data,index=new_index)

df.drop(3,inplace=True)

df.reset_index()
# changing index
df.reset_index()
