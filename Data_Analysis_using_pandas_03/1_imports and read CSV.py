# IMPORTS
import pandas as pd
import plotly.express as px

# create a DataFrame

import pandas as pd
import numpy as np

data = {
    "Order_ID": range(1, 11),
    "Customer_Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack'],
    "Product": ['Laptop', 'Laptop', 'Phone', 'Tablet', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    "Category": ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    "Order_Amount": [1200, 1300, 800, 600, 650, 1150, 900, 700, 1400, 850],
    "Discount": [100, 150, 50, 20, 30, 80, 60, 40, 200, 50],
    "Order_Date": pd.date_range(start='2024-01-01', periods=10, freq='W'),
    "Region": ['North', 'South', 'East', 'North', 'South', 'East', 'North', 'West', 'West', 'East']
}

df = pd.DataFrame(data)
print(df)

# Exploring the DataFrame

df.shape
df.head()
df.tail()
df.count()
df.describe()
df.info()
len(df)
df.columns
df.dtypes
df.isnull().sum()


