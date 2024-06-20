# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:05:14 2024

@author: user
"""

# =============================================================================
'''
Virtual DAC
'''
# =============================================================================

dac_analog=0
def dac_analog_func(dac,max_volts): 
    if dac >=0 & dac < (2**10):
       dac_analog = (dac/(2**10-1))*max_volts
    else:
          raise ValueError(f"{dac} must be more than 0 and less than 1024")

    return round(dac_analog,2)

dac_analog_func(400,5)