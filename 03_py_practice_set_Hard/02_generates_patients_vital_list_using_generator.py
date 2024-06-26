# =============================================================================
# Create a function which generates patient vital data each minutes and store in a list. 
# Every minutes list should be refreshed with new data. 
# 	Data:
# 		1.patient_id,
# 		2.HR
# 		3.RR
# 		4.SPO2
# generate data and store the data in PLSQL
# =============================================================================

import random
import time
from datetime import datetime

# PLSQL CONNECTION
import psycopg2
import pandas as pd

# connection details
try:
    with psycopg2.connect( 
            dbname='mydatabase',
            user='postgres',
            password='Jaimatadi@123',
            host='localhost',
            port='5432'
            ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                            select * from t_emp
                            ''')
                                                
            t_emp=pd.DataFrame(cursor.fetchall())
            print(t_emp)
    
except Exception as e:
    print(f'connection failed,Recevied error as {e}')





def data_generator_func(n):
    dict_patient={}
    dict_patient['patient_id']=f'pa_{n}'
    dict_patient['heart_rate']=random.randint(60,120)
    dict_patient['RR']=random.randint(12,25)
    dict_patient['SP02']=random.randint(80,100)
    dict_patient['dt_created']= datetime.now().strftime('%d/%m/%Y''T''%H:%M:%S')
    yield dict_patient

date_limit=0
data_list=[]
while date_limit < 10000:
    for x in range (1,10+1):   
        data=data_generator_func(x)
        print(next(data))
        data_list.append(data)
        # date_limit+=1
    time.sleep(30)
    

    
    

