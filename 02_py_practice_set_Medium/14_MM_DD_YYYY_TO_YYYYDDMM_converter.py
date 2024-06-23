# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:27:53 2024

@author: user
"""

# =============================================================================
# Create a function that converts a date formatted as 
# MM/DD/YYYY to YYYYDDMM.
# =============================================================================

def MM_DD_YYYY_TO_YYYYDDMM_converter(MM_DD_YYYY):
    MM= MM_DD_YYYY[:2]
    DD= MM_DD_YYYY[3:5]
    YYYY=MM_DD_YYYY[6:]
    YYYYDDMM=YYYY+DD+MM
    return f'MM/DD/YYYY to YYYYDDMM is {YYYYDDMM}'

result=MM_DD_YYYY_TO_YYYYDDMM_converter("12/31/2019")
print(result)

