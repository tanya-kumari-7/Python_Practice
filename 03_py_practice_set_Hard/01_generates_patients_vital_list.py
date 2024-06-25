# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:59:57 2024

@author: user
"""

# =============================================================================
# Create a function which generates patient vital data each minutes and store in a list. 
# Every minutes list should be refreshed with new data. 
# 	Data:
# 		1.patient_id,
# 		2.HR
# 		3.RR
# 		4.SPO2
# =============================================================================

import random
import time
from datetime import datetime

def data_generator_func(n):
    dict_patient={}
    dict_patient['patient_id']=f'pa_{n}'
    dict_patient['heart_rate']=random.randint(60,120)
    dict_patient['RR']=random.randint(12,25)
    dict_patient['SP02']=random.randint(80,100)
    dict_patient['dt_created']= datetime.now().strftime('%d/%m/%Y''T''%H:%M:%S' )
    return dict_patient

list_of_patient=[]
end=0
while end != 5:
        for x in range (1,11): # for 10 patient data
            data=data_generator_func(x)
            list_of_patient.append(data)
        print(list_of_patient)
        time.sleep(60)
        list_of_patient.clear()
        end+= 1
        print(f'{end} is end')

    
    

