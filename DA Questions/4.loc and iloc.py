''' Q2. Explain the difference between iloc[] and loc[] in Pandas.'''

import pandas as pd

data = {
        'Name':['sonam','monam','tonam','ponam','lonam'],
        'age':[10,15,20,25,30],
        'page':[10,20,30,40,50]
        }

df = pd.DataFrame(data)
print(df)

# Select row with index '1'
df.loc[1]

# Select rows 'a' and 'c'
df.loc[[0, 4]]

# Select the 'Name' and 'Age' columns for rows 1 and 2 index
df.loc[[1, 2], ['Name', 'age']]


# Select rows from 1 to 3 and columns from 'Name' to 'Age'
df.loc[1:3, 'Name':'age']

# Select rows where Age > 30
df.loc[df['age'] > 20]

# Select the second row (index 1)
df.iloc[1]

# Select the first and third rows
df.iloc[[0, 2]]

# Select the first two rows and first two columns
df.iloc[:2, :2]

# Select rows from index 0 to 2 and columns from index 0 to 1
df.iloc[0:3, 0:2]

# Get indexes where Age > 30 using iloc
df.iloc[(df['age'] > 20).values]






