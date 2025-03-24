''' Q9. How can you identify and remove duplicate rows in a DataFrame?'''

import pandas as pd
import numpy as np

data = {
    'Name': ['John', 'Anna', 'Mike', 'Sara', 'John', 'Mike'],
    'Age': [28, 22, 35, 32, 28, 35],
    'City': ['NY', 'LA', 'SF', 'TX', 'NY', 'SF']
}

df1=pd.DataFrame(data)

df1.duplicated()

duplicate = df1[df1.duplicated(keep=False)]
duplicate = df1[df1.duplicated(keep='last')]
duplicate = df1[df1.duplicated(keep='first')]
duplicate = df1[df1.duplicated(subset='City',keep=False)]


