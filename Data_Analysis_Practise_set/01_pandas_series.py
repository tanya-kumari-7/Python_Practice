# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:39:37 2024

@author: user
"""
import pandas as pd

'''
1.
Create and display a one-dimensional and two dimensional array-like 
object containing an array of data.

'''

one_dimensional_series=pd.Series([100,200,300,400,500])
print(one_dimensional_series)

two_dimensional_series=pd.Series([100,200,300,400,500],['sonam','tanya','gaurav','nitin','sony'])
print(two_dimensional_series)

'''
2.
Write a Pandas program to convert a Panda module Series to Python
list and it’s type.

'''
one_dimensional_series_to_list=one_dimensional_series.to_list()
print(one_dimensional_series_to_list)
print(type(one_dimensional_series_to_list))

'''
3.
Write a Pandas program to add, subtract, multiple and divide two 
Pandas Series.
'''
ds1=pd.Series([100,200,300,400])
ds2=pd.Series([2,4,6,8])

ds_add = ds1 + ds2
print(ds_add)

ds_sub = ds1 - ds2
print(ds_sub)

ds_multiple = ds1 * ds2
print(ds_multiple)

ds_divide = ds1 / ds2
print(ds_divide)

'''
4.
Write a Pandas program to compare the elements of the two Pandas 
Series.
'''
ds_equal = ds1 == ds2
ds_equal

ds_greater = ds1 > ds2
ds_greater

ds_smaller = ds1 < ds2
ds_smaller

'''
5.
Write a Pandas program to convert a dictionary to a Pandas series.
Sample dictionary: d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
'''
dict_1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
dict_1
dict_1_to_series=pd.Series(dict_1)
dict_1_to_series

'''
6.
Write a Pandas program to convert a NumPy array to a Pandas series.
Sample NumPy array: d1 = [10, 20, 30, 40, 50]
'''
d1 = [10, 20, 30, 40, 50]
d1
d1_to_series=pd.Series(d1)
d1_to_series

'''
7.
Write a Pandas program to change the data type of given a column 
or a Series.

Sample Series:
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Change the said data type to numeric:
0 100.00
1 200.00
2 NaN
3 300.12
4 400.00
dtype: float64
'''
sample_1=pd.Series(['100', '200', 'python', '300.12', '400'])
sample_1
sample_1_int=pd.to_numeric(sample_1,errors='coerce') 
#errors='coerce' is used to handle diffrent datatype. 
sample_1_int

'''
8.
Write a Pandas program to convert the first column of a DataFrame as a Series.
'''

# Creating a dataFrame
data=[
      {'name':'sonam','mobile':'9999999999'},
      {'name':'gaurav','mobile':'9999999998'},
      {'name':'nitin','mobile':'9999999993'},
      {'name':'sony','mobile':'9999999998'},
      {'name':'mony','mobile':'9999999994'},
        ]

df=pd.DataFrame(data)
df

# Changing data frame column into series
df_name_to_series=pd.Series(df['name'])
type(df_name_to_series)

# geting one row using iloc
df_iloc=df.iloc[0:2]
df_iloc

'''
Write a Pandas program to convert a given Series to an array.
'''
df_name_to_series_into_array= df_name_to_series.values
