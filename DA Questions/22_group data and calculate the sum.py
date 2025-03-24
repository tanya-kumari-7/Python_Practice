'''Q11. How do you group data and calculate the sum?'''

import pandas as pd
import numpy as np

data = {
    'Name': ['John', 'Anna', 'Mike', 'Sara', 'John', 'Mike'],
    'Age': [28, 22, 35, 32, 28, 35],
    'City': ['NY', 'LA', 'SF', 'TX', 'NY', 'SF']
}

df1=pd.DataFrame(data)

df1.groupby('City')['Age'].sum()
