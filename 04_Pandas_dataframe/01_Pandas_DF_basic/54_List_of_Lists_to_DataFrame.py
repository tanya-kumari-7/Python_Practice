
# =============================================================================
'''
Write a Pandas program to convert a given list of 
lists into a Dataframe.
'''
# =============================================================================
import pandas as pd
import numpy as np

my_lists = [['col1', 'col2'], [2, 4], [1, 3]]
df=pd.DataFrame(columns=my_lists[0],data=my_lists[1:])
