
# =============================================================================
'''
Join two dataframe 
'''
# =============================================================================
import pandas as pd
import numpy as np

exam_data1 = {
    'id' :[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df1=pd.DataFrame(exam_data1,index=labels)

exam_data2 = {
    'id' :[1011,1012,1003,1014,1005,1006,1017,1008,1009,1010],
    'name': ['sonam', 'tanya', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12, 9, 16, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2=pd.DataFrame(exam_data2,index=labels)

########### INNER JOIN 
inner_df=df1.merge(df2,how= 'inner',on=['id'])
inner_df.head(5)

inner_df2=df1.merge(df2,how= 'inner',on=['id','name'],sort=True)
inner_df2

################### OUTER JOIN 

outer_df = df1.merge(df2,how= 'outer',on=['id'],sort=True)
outer_df

#################### LEFT JOIN 

left_df = df1.merge(df2,how='left',on=['id'])
left_df

##################### Right join 
right_df = df1.merge(df2,how='right',on=['id'])
right_df


