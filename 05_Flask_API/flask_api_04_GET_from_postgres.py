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

@app.route('/emp',methods=['Get'] )

def get_api():
    connect=psycopg2.connect(**postgres)
    cur=connect.cursor()
    cur.execute('select * from t_emp')
    df=pd.DataFrame(cur.fetchall())
    #data=request.get_json()
    data=df.head(2)
    data = data.to_json(orient='records')
    return data



if __name__ == '__main__':
    app.run(debug=False)







