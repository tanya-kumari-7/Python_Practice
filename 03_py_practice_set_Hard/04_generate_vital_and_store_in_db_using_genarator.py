# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:58:48 2024

@author: user
"""

# important libery
import psycopg2
import pandas as pd
import random
import time
from datetime import datetime

def create_db_connection():
    conn= psycopg2.connect(
            dbname='mydatabase',
            user='postgres',
            password='Jaimatadi@123',
            host='localhost',
            port='5432'
            )
    return conn
    
def insert_in_table(connection, vital_dic):
    # SQL insert query
    insert_into_py_patient_tbl = '''
        INSERT INTO py_patient_tbl
        (patient_id, heart_rate, RR, sp02, dt_created)
        VALUES (%(patient_id)s, %(heart_rate)s, %(RR)s, %(SP02)s, %(dt_created)s);
    '''   
    # conneting python to postgres
    try:
        with connection.cursor() as cursor:
            # execute the cursor
            # cursor.execute(create_or_replace_tbl)
            cursor.execute(insert_into_py_patient_tbl,vital_dic)
            print('data inserted successfuly')
        print(cursor)
    except Exception as e:
        print(f'Connection failed, received error: {e}')

# Generating the data using function
def data_generator_func(n):
    dict_patient={}
    for x in range(1,n+1):
        dict_patient['patient_id']=f'pa_{x}'
        dict_patient['heart_rate']=random.randint(60,120)
        dict_patient['RR']=random.randint(12,25)
        dict_patient['SP02']=random.randint(80,100)
        dict_patient['dt_created']= datetime.now().strftime('%d/%m/%Y''T''%H:%M:%S')
        yield dict_patient

num=input('Enter number of patient:') 
num=int(num)
a = data_generator_func(num)
i=0
connection = create_db_connection()
while i < num:
    print(next(a))
    insert_in_table(connection, next(a))
    i+=1


