# =============================================================================
'''
Grouping and Aggregation:
Sample Data: A DataFrame df with columns Category (categorical),
Value (numeric).
Question: Calculate the average Value for each Category.
''' 
# =============================================================================

import pandas as pd
import numpy as np

exam_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [60000, 80000, 75000, 90000, 50000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Experience': [3, 7, 5, 4, 2]
        }
labels = [1,2,3,4,5]

df=pd.DataFrame(exam_data,index=labels)
print(df)

# AVG salary of emp in each department
Department_wise_avg_salary=df.groupby('Department').mean('Salary').reset_index()
print(Department_wise_avg_salary[['Department','Salary']])

