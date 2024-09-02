import psycopg2
import pandas as pd
import requests
from flask import Flask,request

# Geting Data from Open source api--------------------------------------

from pandas import json_normalize #to normalize dict inside dict
api='https://instagram243.p.rapidapi.com/searchlocation/paris'
headers={
    'x-rapidapi-host': 'instagram243.p.rapidapi.com',
    'x-rapidapi-key':'236468e9a5msh539c0273f05d5a9p1d157cjsn0ad96f67d2f2'
    }

response= requests.get(api,headers=headers)
data=response.json()
print(data)
df = json_normalize(data.get('data'))
df.columns
# ----------------------------------------API-------------
# including postgres connection

postgres = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'Jaimatadi@123',
    'host': 'localhost',
    'port': '5432'
}

app=Flask(__name__)
@app.route('/searchlocation/paris',methods=['POST'])

def post_api():
    conn=psycopg2.connect(** postgres)
    cur=conn.cursor()
    
    for index, row in df.iterrows():
        title_ = row['title']
        subtitle_ = row['subtitle']
        location_pk_ = row['location.pk']
        location_short_name_ = row['location.short_name']
        # print(title_, subtitle_, location_pk_, location_short_name_)
        
        query='''
            insert into api_searchlocation_paris (title, subtitle, location_pk, location_short_name)
            values(%s,%s,%s,%s)
           '''
        cur.execute(query,(title_, subtitle_, location_pk_, location_short_name_))
        conn.commit()
        
    api_response={}
    api_response['msg']='post successful'
    api_response['data']=data
    print(response)
    cur.close()
    conn.close()
    
    return api_response


app.run(debug=False)
    
    


