# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 23:06:26 2024

@author: user
"""

import psycopg2
import pandas as pd
from flask import Flask,request

# connection to postgres

postgres={
    'dbname':'mydatabase',
    'user':'postgres',
    'password':'Jaimatadi@123',
    'host':'localhost',
    'port':'5432'
    }



# Create a get API


app=Flask(__name__)

@app.route('/emp_post',methods=['POST'] )

def get_api():
    response={}
    connect=psycopg2.connect(**postgres)
    cur=connect.cursor()
    data=request.get_json()
    name=data.get('name')
    age=data.get('age')
    email=data.get('email')
    print(name,age,email)
    try:
        cur.execute('''
               INSERT INTO public.api_table (name, age, email) 
               VALUES (%s, %s, %s)
           ''', (name, age, email))
    except Exception as e:
        print("there is an error ", e)
     # Commit changes to the database
    connect.commit()
    cur.close()
    connect.close()
    
    response['msg']='set'
    response['data']=data
    
    return response
    

if __name__ == '__main__':
    app.run(debug=False)







