# important libery
import psycopg2
import pandas as pd
import random
import time
from datetime import datetime

# Generating the data using function
def data_generator_func(n):
    dict_patient={}
    dict_patient['patient_id']=f'pa_{n}'
    dict_patient['heart_rate']=random.randint(60,120)
    dict_patient['RR']=random.randint(12,25)
    dict_patient['SP02']=random.randint(80,100)
    dict_patient['dt_created']= datetime.now().strftime('%d/%m/%Y''T''%H:%M:%S')
    return dict_patient

# calling the function
data_limit=0
list_1=[] 
for x in range(1,200):
    data=data_generator_func(x)
    list_1.append(data)
    data_limit+=1
    print(list_1)
    print(data_limit)
    # time.sleep(3)

# table creation 
create_or_replace_tbl='''
    CREATE TABLE py_patient_tbl (
    patient_id VARCHAR,
    heart_rate INT,
    RR INT,
    sp02 INT,
    dt_created TIMESTAMP);
'''
# SQL insert query
insert_into_py_patient_tbl = '''
    INSERT INTO py_patient_tbl
    (patient_id, heart_rate, RR, sp02, dt_created)
    VALUES (%(patient_id)s, %(heart_rate)s, %(RR)s, %(SP02)s, %(dt_created)s);
'''


    
# conneting python to postgres
try:
    # creating connection
    with psycopg2.connect(
            dbname='mydatabase',
            user='postgres',
            password='Jaimatadi@123',
            host='localhost',
            port='5432'
            ) as connection:
        # creating cursor
        with connection.cursor() as cursor:
            # execute the cursor
            # cursor.execute(create_or_replace_tbl)
            cursor.executemany(insert_into_py_patient_tbl,list_1)
            print('data inserted successfuly')
    
except Exception as e:
    print(f'Connection failed, received error: {e}')
