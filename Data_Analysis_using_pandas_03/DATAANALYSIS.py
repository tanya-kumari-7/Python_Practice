# IMPORTS
import pandas as pd
import plotly.express as px

# create a DataFrame

import pandas as pd
import numpy as np


data = {
    "Order_ID": [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],  # Duplicating Order_IDs 1 and 10
    "Customer_Name": ['Alice', 'Alice', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Ivan'],
    "Product": ['Laptop', 'Laptop', 'Laptop', 'Laptop', 'Phone', 'Tablet', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Laptop'],
    "Category": ['Electronics'] * 12,
    "Order_Amount": [1200, 1200, 1200, 1300, 800, 600, 650, 1150, 900, 700, 1400, 1400],
    "Discount": [100, 100, 100, 150, 50, 20, 30, 80, 60, 40, 200, 200],
    "Order_Date": pd.date_range(start='2024-01-01', periods=12, freq='W'),
    "Region": ['North', 'North', 'North', 'South', 'East', 'North', 'South', 'East', 'North', 'West', 'West', 'West']
}
df = pd.DataFrame(data)
print(df)

# Exploring the DataFrame

# basic information about the DataFrame
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

# Checking for duplicates

for col in df.columns:
    total_value = df[col].shape[0]
    unique_value = df[col].nunique()
    duplicate_count = total_value - unique_value
    print(f"Column '{col}' has {duplicate_count} duplicates.")

# get the duplicate rows
duplicates = df[df.duplicated()]
print("Duplicate Rows:" , duplicates)

duplicates = df[df.duplicated(keep=False)]
print(duplicates)

duplicates = df[df.duplicated(subset='Order_ID', keep=False)]
print(duplicates)

len(df)

# updating the id for the duplicate rows
df[(df["Order_ID"] == 1) & (df["Order_Date"] == '2024-01-07')]
df.loc[(df["Order_ID"]==1) & (df["Order_Date"] == '2024-01-07'), "Order_ID"] = 11

df[(df["Order_ID"]==10) & (df["Order_Date"] == "2024-03-17")]
df.loc[(df["Order_ID"]==10) & (df["Order_Date"] == "2024-03-17"),"Order_ID"]= 12

df[(df["Order_ID"] == 1)]
df[(df["Order_ID"] == 10)]


df.columns
df

# Exploring data from the DataFrame
df['Product'].unique()
df['Product'].nunique()
df['Product'].value_counts()
df['Product'].value_counts(normalize=True)
df['Product'].value_counts().plot(kind='bar')

# filtering the DataFrame

 # Orders above 1000
 df[df["Order_Amount"]>1000]
df[df["Order_Amount"]<1000]

# Creating a new column using Order_Amount
df["Order_Amount_Group"] = df["Order_Amount"].apply(lambda x: "High" if x > 1000 else "Low")

def get_category(row):
   if row["Order_Amount"] > 1000 and row["Discount"] > 100:
       return "Premium"
   elif row["Order_Amount"] > 1000 and row["Discount"] <= 100:
       return "Standard"

df['order_category'] = df.apply(get_category, axis=1)
df.columns
df

df[df["order_category"] == "Premium"]
df[df["order_category"] == "Standard"]
df[df["Order_Amount"] > 1000][["Order_ID", "Customer_Name", "Product", "Order_Amount"]]
df[df["order_category"].isna()]


