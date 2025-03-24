''' Q10. How do you convert a column’s data type (e.g., string to datetime)?'''

import pandas as pd
import numpy as np

data = {
    'Name': ['John', 'Anna', 'Mike', 'Sara', 'John', 'Mike'],
    'Age': [28, 22, 35, 32, 28, 35],
    'City': ['NY', 'LA', 'SF', 'TX', 'NY', 'SF']
}

df1=pd.DataFrame(data)

df2 = df1['Age'].astype(str)
