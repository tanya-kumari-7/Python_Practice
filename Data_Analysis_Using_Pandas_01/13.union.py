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
df.info()
avg_salary_by_department = '''
    SELECT 
        Department,
        round(Avg(Salary)) as Avg_salary
    FROM df
    WHERE Department IS NOT NULL
    GROUP BY 1
    ORDER BY 2 desc
'''
sqldf(avg_salary_by_department,locals())

#  Method 2 using dataframe
df.groupby (["Department"])\
    .agg({"Salary":'mean'})
    
    
# Task 7: Filter and Display IT Department Employees.
emp_from_IT_department = '''
    SELECT * FROM df
    WHERE Department = 'IT'
'''
sqldf(emp_from_IT_department , locals())

# menthod 2 using dataframe
df[df['Department'] == 'IT']

# Task 8: Add 10% Bonus to Salaries.
bonus = '''
        SELECT 
            *,
            (Salary * 10)/100 as Bonus,
            Salary + (Salary *10)/100 as New_Salary
        FROM df
'''
new_df = sqldf(bonus.lower())


#  Method 2 
df['Bonus'] = (df['Salary']*10)/100
df.info()
df['New_salary'] = df["Salary"] + (df["Salary"]*10)/100
df.info()


# Method 3 Createing a functions
df_new = df
df_new = pd.DataFrame(df_new)
df.info()
df_new.info()
def bonus_and_new_salary_cal(old_salary):
    bonus = (old_salary * 10)/100
    New_salary = old_salary + (old_salary *10)/100
    return bonus,New_salary 

df_new[["Bonus","New_salary"]]= new_df['Salary']\
    .apply(bonus_and_new_salary_cal).apply(pd.Series)

df_new.info()
df_new.head(5)


# Method 4 using lambda functions

df3= df

df3[["Bonus","New_Salary"]] = df["Salary"]\
    .apply(lambda x: pd.Series(bonus_and_new_salary_cal(x)))
    
df3.info()

# Task 9: Find Maximum Salary by Age.

max_salary_by_age = '''
        SELECT 
            Age,
            max(Salary) as max_salary_by_age
        FROM df
        Group by 1 
        ORDER BY 2 DESC
'''
sqldf(max_salary_by_age,locals())

#  Method 2 using pandas 
df.groupby(['Age']).max("Salary").reset_index()

# Task 10: Self-Join on Employee Data.
df.info()
df2.info()

self_join = '''
    SELECT * FROM df self join df as df2
'''
sqldf(self_join,locals())

#  merge
df.info()
df_inner = df.merge(df2,how= 'inner',on='Emp_No')
df_left = df.merge(df2,how='left',on='Emp_No')
df_right = df.merge(df2,how='right',on='Emp_No')
df_outer = df.merge(df2,how='outer',on='Emp_No')
df_cross = df.merge(df2,how='cross')

# Joins
pd_inner = df.set_index('Emp_No')\
    .join(df2.set_index('Emp_No'),how='inner',lsuffix = "_L",rsuffix = '_r')
pd_outer = df.set_index("Emp_No")\
    .join(df2.set_index('Emp_No'),how='outer',lsuffix='_l',rsuffix='_r')
pd_left = df.set_index("Emp_No")\
    .join(df2.set_index("Emp_No"),how='left',lsuffix='_l',rsuffix='_r')
pd_right =df.set_index('Emp_No')\
    .join(df2.set_index("Emp_No"),how='right',lsuffix='_l',rsuffix='_r')   
pd_cross = df.set_index('Emp_No')\
    .join(df2.set_index("Emp_No"),how='cross',lsuffix='_l',rsuffix='_r')

union_tbl = pd.concat([df,df2])

# Task 11: Calculate Average Employee Age.
# Task 12: Calculate Total Salary by Department.
# Task 13: Sort Data by Age and Salary.
# Task 14: Count Employees in Each Department.
# Task 15: Filter Employees with the letter o in the Name.



df_schema = df.info()