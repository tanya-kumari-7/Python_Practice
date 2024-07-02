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
9.
Write a Pandas program to convert a given Series to an array.
'''
df_name_to_series_into_array= df_name_to_series.values

'''
10.
Write a Pandas program to convert Series of lists to one Series.
'''
s1 = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])

# converted s1 into row and column
series_of_list_to_one_series=s1.apply(pd.Series) 
#converted columns into row
series_of_list_to_one_series=s1.apply(pd.Series).stack() 

# dropped column index and create on series
series_of_list_to_one_series=s1.apply(pd.Series).stack().reset_index(drop=True)

series_of_list_to_one_series

'''
11.
Write a Pandas program to sort a given Series.
'''
# By default sort_values() is asc 
series_sorting_asc=series_of_list_to_one_series.sort_values()
# series sorting desc
series_sorting_desc=series_of_list_to_one_series.sort_values(ascending=False)

'''
12.
Write a Pandas program to add some data to an existing Series.
'''
# adding some value to each item in the series 
adding_data_to_series1=series_of_list_to_one_series.add('_sonam')

# use concat (existing series + crete new series using list)
# to ignore new added series indexing use(ignore_index=True)
adding_data_to_series2=pd.concat([series_of_list_to_one_series,pd.Series([500,'mony'])],ignore_index=True)


'''
13.
Write a Pandas program to create a subset of a given series based 
on value and condition.
'''
s1 = pd.Series([00,100,200,300,400,5,6,700,8,9,10000])
s2=s1[s1<50]

'''
14.
Write a Pandas program to change the order of index of a given 
series.
'''
# createing series with defined index (use data= [],index=[])
s1 = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])

# re-arraging the index of series
# Data Series after changing the order of index:
s2=s1.reindex(index=['B','A','C','D','E'])

'''
15.
Write a Pandas program to create the mean and standard deviation 
of the data of a given Series.
'''
s1 = pd.Series([00,100,200,300,400,5,6,700,8,9,10000])
s1_mean=s1.mean()
s1_std=s1.std()

'''
16.
Write a Pandas program to get the items of a given series not 
present in another given series.
'''
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])

s3= sr1[~sr1.isin(sr2)]

'''
17.
Write a Pandas program to get the items which are not common of 
two given series.
'''
sr1_unique = sr1[~sr1.isin(sr2)]
sr2_unique=sr2[~sr2.isin(sr1)]

# always give concat in a list[]
unique=pd.concat([sr1_unique,sr2_unique])


'''
18.
Write a Pandas program to compute the minimum, 25th percentile, 
median, 75th, and maximum of a given series.
'''
s1
s1_minimum=s1.min()
s1_maximun=s1.max()
s1_median=s1.median()
s1_25th_percentile=s1.quantile([0.25,0.50,0.75])



'''
19.
Write a Pandas program to calculate the frequency counts of 
each unique value of a given series.
'''

'''
20.

'''









