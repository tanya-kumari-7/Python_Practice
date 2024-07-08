# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:39:37 2024

@author: user
"""
import pandas as pd
import numpy as np

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
# ~: This is the bitwise NOT operator. It inverts the 
# boolean values. True becomes False, and False becomes True. 

sr1_unique = sr1[~sr1.isin(sr2)]
sr2_unique=sr2[~sr2.isin(sr1)]
sr2_unique=sr2[sr2.isin(sr1)]

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
list_num_series=pd.Series([1,2,3,5,6,5,4,3,2,1])
vaue_count=list_num_series.value_counts()

'''
20.
Write a Pandas program to display most frequent value in a 
given series and replace everything else as ‘Other’ in the 
series.
'''
data = pd.Series(
    ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'kiwi'
     ]
    )
most_frequent =data.value_counts().idxmax()
result=[]
for x in data:
    if x == most_frequent:
        result.append(x)
    else:
        result.append('other')
        
print(result)

"""
21.
Write a  Pandas program to find the positions of numbers 
that are multiples of 5 of a given series.
"""
# Find Positions: Use np.where to identify the positions 
# where the values in the series are multiples of 5. 
num_series = pd.Series(np.random.randint(1, 10, 9))
result=np.where(num_series % 5 ==0)[0]

"""
22.
Write a Pandas program to extract items at given positions 
of a given series.
"""
#  use of .take(index)
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]

items_with_given_index_value=num_series.take(element_pos)

"""
23.
Write a Pandas program to get the positions of 
items of a given series in another given series.
"""
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
postition_of_s1_in_s2= series1[series1.isin(series2)].index

"""
24.
Write a  Pandas program convert the first and last character 
of each word to upper case in each word of a given series.

"""
data
result=[]
for x in data:
    y=x[0].upper() + x[1:-1] + x[-1].upper()
    result.append(y)
    
"""
25.
Write a  Pandas program to calculate the number of 
characters in each word in a given series.
"""
data
data_dic={}

for x in data:
    data_dic[x]=len(x)
print(pd.Series(data_dic))

"""
26.
Write a Pandas program to compute difference of differences 
between consecutive numbers of a given series.
"""
series1 = pd.Series([1, 3, 5, 8, 10, 11, 15])
#  calculate diffrence bwetween two numbers
diff_series=(series1.diff()).tolist()
diff_of_diff=series1.diff().diff().tolist()
diff_of_diff

"""
27.
Write a Pandas program to convert a series of date 
strings to a timeseries.
"""
# Sample data
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])

# Function to parse dates
def parse_date(date_str):
    formats = ["%d %b %Y", "%d-%m-%Y", "%Y%m%d", "%Y/%m/%d", "%Y-%m-%d", "%Y-%m-%dT%H:%M"]
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    return pd.NaT

# Apply the parsing function to the series
datetime_series = date_series.apply(parse_date)
print(datetime_series)

"""
28.
Write a  Pandas program to get the day of month, day of year, 
week number and day of week from a given series of date 
strings.
"""
date_series

day_of_month=date_series.dt.day.tolist()
day_of_month

day_of_year=date_series.dt.dayofyear.tolist()
day_of_year

day_of_week=date_series.dt.dayofweek.tolist()
day_of_week


"""
29.
Write a  Pandas program to convert year-month 
string to dates adding a specified day of the month.
"""

date_series = pd.Series(
    ['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'
     ])

datetime_series=pd.to_datetime(date_series,errors='coerce')
datetime_series

"""
30.
Write a Pandas program to filter words from a given series 
that contain atleast two vowels.
"""
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
vowels=['a','e','i','o','u']
result=[]
working={x:0 for x in color_series}
for x in color_series:
    for y in x.lower():
        if y in vowels:
            working[x] +=1
        else :
            continue
result=[x for x in working if working[x] >=2]
            
"""
31.
Write a Pandas program to compute the Euclidean distance 
between two given series.
"""


"""
32.

"""
"""
33.

"""
"""
34.

"""
"""
35.

"""
"""
36.

"""
"""
37.

"""
"""
38.

"""
"""
39.

"""
"""
40.

"""
        








