import psycopg2
import pandas as pd
from flask import Flask,request,jsonify
import json

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
    
    cur.execute ('''
                INSERT INTO py_patient_tbl (patient_id, heart_rate, rr, sp02, dt_created)
                values (%s,%s,%s,%s,%s)
       ''',(patient_id, heart_rate, rr, sp02, dt_created))
       
    conn.commit() 
    response={}
    response['msg']='post successful'
    response['data']=data
    print(response)
    
    cur.close()
    conn.close()
    
    return response


# -----------------------------------GET All api

app=Flask(__name__)
@app.route('/patient', methods=['GET'])

def get_api():
    
    conn = psycopg2.connect(** postgres)
    cur = conn.cursor()
    
    ## Request parsing
    data = request.get_json()
    patient_id = data.get("patient_id")
    
    ## Get data from DB
    print(patient_id)
    query = f"SELECT patient_id, heart_rate FROM py_patient_tbl where patient_id = '{patient_id}'"
    print(query)
    cur.execute(query)
    results=cur.fetchall()
    print(results)
   
   
    # Map result
    mapped_results = [map_row_to_structure(row) for row in results]

    print("mapped result is", mapped_results)
    
    conn.commit()
    
    ## Return
    response={}
    response['msg']='get successful'
    response['data']=mapped_results
    print(response)
    
    cur.close()
    conn.close()
    
    return response

 
def map_row_to_structure(row):
    return {
        'patient_id': row[0],
        'heart_rate': row[1]
    }

if __name__ == "__main__":
    app.run(debug=False)

     
    

