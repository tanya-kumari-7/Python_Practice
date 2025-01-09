# Important Library

import pandas as pd 
import numpy as np
import matplotlib as mt
import seaborn as sea

# Reding CSC

csv = pd.read_csv(r"C:/Users/user/Downloads/employees.csv")
df= pd.DataFrame(csv)
print(df)
