import psycopg2
import pandas as pd
from flask import Flask,request

postgres = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'Jaimatadi@123',
    'host': 'localhost',
    'port': '5432'
}

# --------------POST API

app=Flask(__name__)
@app.route('/patient', methods=['POST'])

def Post_api():
    
    conn = psycopg2.connect(** postgres)
    cur = conn.cursor()
    
    data = request.get_json()
    patient_id = data.get("patient_id")
    heart_rate = data.get("heart_rate")
    rr = data.get("rr")
    sp02 = data.get("sp02")
    dt_created = data.get("dt_created")
    print(patient_id, heart_rate, rr, sp02, dt_created)
    
    cur.execute('''
                INSERT INTO py_patient_tbl 
        
       ''' )
    

