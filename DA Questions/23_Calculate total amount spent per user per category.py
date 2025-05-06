"""
1. Complex GroupBy Aggregation
Difficulty: 🔥🔥🔥🔥
Topic: Pandas, Data Aggregation
Problem:
Given a large dataset of e-commerce transactions with columns:
['user_id', 'product_id', 'category', 'amount', 'timestamp']
Write a function to:

Calculate total amount spent per user per category.

Return top 3 users with the highest spending in each category.
"""
import pandas as pd
from datetime import datetime

# Sample data
data = [
    [101, 'P001', 'Electronics', 250.00, datetime(2023, 5, 1, 14, 30)],
    [102, 'P002', 'Groceries', 45.50, datetime(2023, 5, 2, 10, 15)],
    [103, 'P003', 'Clothing', 99.99, datetime(2023, 5, 2, 16, 45)],
    [101, 'P004', 'Electronics', 300.00, datetime(2023, 5, 3, 9, 0)],
    [104, 'P005', 'Groceries', 20.00, datetime(2023, 5, 4, 12, 0)]
]

# Column names
columns = ['user_id', 'product_id', 'category', 'amount', 'timestamp']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Function to calculate total amount spent per user per category


def  calculate_total_spend_per_user_per_category(df):
    total_spent_per_user_per_category = df.groupby(["user_id","category"]).sum("amount").reset_index()
    return total_spent_per_user_per_category

output = calculate_total_spend_per_user_per_category(df)
print(output)

