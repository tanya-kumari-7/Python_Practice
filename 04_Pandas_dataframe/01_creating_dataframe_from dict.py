# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:39:16 2024

@author: user
"""

# =============================================================================
'''
1.
Write a Pandas program to create a dataframe from a dictionary 
and display it.
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
'''
# =============================================================================
import pandas as pd

sample_dic={
    'X':[78,85,96,80,86],
    'Y':[84,94,89,83,86],
    'Z':[86,97,96,72,83]
    }
df=pd.DataFrame(sample_dic)
print(df)
