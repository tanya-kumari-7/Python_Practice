import psycopg2
import pandas as pd
from flask import Flask,request,jsonify

postgres = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'Jaimatadi@123',
    'host': 'localhost',
    'port': '5432'
}


app= Flask(__name__)

@app.route('/paris', methods=['GET'])
def get_api():
    
    conn = psycopg2.connect(** postgres)
    cur = conn.cursor()
    data = request.get_json()
    get_key = data.get('location_pk')
    print(get_key)
    
    query = '''
    SELECT title, location_pk FROM api_searchlocation_paris where location_pk = %s
    '''
    cur.execute(query,(get_key,))
    
    get_data = cur.fetchall()
    print(get_data)
    mapped_data = [map_row_to_structure(row) for row in get_data]
    print(mapped_data)
    
    response = {}
    response['Msg'] ='Get Success'
    response['data'] = mapped_data
    
    cur.close()
    conn.close()

    return jsonify(response) 
    
# --------------------------------------- Put


@app.route('/paris', methods=['PUT'])
def put_api():
    
    conn = psycopg2.connect(** postgres)
    cur = conn.cursor()
    data = request.get_json()
    get_key = data.get('location_pk')
    get_key2 = data.get('title')
    print(get_key)
    
    query = '''
    UPDATE api_searchlocation_paris SET title = %s where location_pk = %s
    '''
    cur.execute(query,(get_key2,get_key,))
    conn.commit()
    
    # get_data = cur.fetchall()
    # print(get_data)
    # mapped_data = [map_row_to_structure(row) for row in get_data]
    # print(mapped_data)
    
    response = {}
    response['Msg'] ='Get Success'
    response['data'] = data
    
    cur.close()
    conn.close()

    return jsonify(response) 
    
# --------------------------------------- PATCH


@app.route('/paris', methods=['PATCH'])
def PATCH_api():
    
    conn = psycopg2.connect(** postgres)
    cur = conn.cursor()
    data = request.get_json()
    location_pk = data.get('location_pk')
    title = data.get('title')
    subtitle = data.get('subtitle')
    
    query = '''
    UPDATE api_searchlocation_paris 
        SET title = %s ,
         subtitle= %s
    where location_pk = %s
    '''
    cur.execute(query,(title,subtitle,location_pk,))
    conn.commit()
    
    # get_data = cur.fetchall()
    # print(get_data)
    # mapped_data = [map_row_to_structure(row) for row in get_data]
    # print(mapped_data)
    
    response = {}
    response['Msg'] ='Get Success'
    response['data'] = data
    
    cur.close()
    conn.close()

    return jsonify(response) 

    
app.run(debug=False)

    
    
def map_row_to_structure(row):
    return {
        'location_pk_': row[0],
        'title_': row[1] }

    
    