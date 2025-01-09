# Important Library

import pandas as pd 
import numpy as np
import matplotlib as mt
import seaborn as sea
from pandasql import sqldf

# Task 1: Generate DataFrame from CSV data.
csv = pd.read_csv(r"C:/Users/user/Downloads/employees.csv")
df= pd.DataFrame(csv)
print(df)

# Task 2: Explore Dataframe.
df.head(5)
df.tail(5)
df.info()
df.isna()
df.isnull().sum()
df.describe()

for col in df.select_dtypes(include=['object','category']):
    print (col)
    print(f'column {col}:')
    print(df[col].count())
    print(df[col].value_counts())
    
duplicate = df[df.duplicated()]
print(duplicate)
print(f'len of dup {len(duplicate)}')
    
# Task 3: Display schema of DataFrame.
print(df.info())
# Task 4: Create a new dataframe.
csv2 = pd.read_csv(r"C:/Users/user/Downloads/employees2.csv")
df2= pd.DataFrame(csv2)
print(df2)

# Task 5: Execute an SQL query.
query = '''
    SELECT * FROM df
'''
sqldf(query,locals())
# Task 6: Calculate Average Salary by Department.
# Task 7: Filter and Display IT Department Employees.
# Task 8: Add 10% Bonus to Salaries.
# Task 9: Find Maximum Salary by Age.
# Task 10: Self-Join on Employee Data.
# Task 11: Calculate Average Employee Age.
# Task 12: Calculate Total Salary by Department.
# Task 13: Sort Data by Age and Salary.
# Task 14: Count Employees in Each Department.
# Task 15: Filter Employees with the letter o in the Name.



df_schema = df.info()