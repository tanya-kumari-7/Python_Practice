from flask import Flask, request, jsonify
import pandas as pd
import psycopg2

postgres = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'Jaimatadi@123',
    'host': 'localhost',
    'port': '5432'
}

app = Flask(__name__)

@app.route("/emp", methods=['POST'])
def POST_api_user():
    conn = psycopg2.connect(**postgres)
    cur = conn.cursor()
    
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    position = data.get('position')
    salary = data.get('salary')
    created_at = data.get('created_at')
    last_updated_at = data.get('last_updated_at')
    print(id, name, position, salary, created_at, last_updated_at)
    cur.execute('''
        INSERT INTO t_emp (id, name, position, salary, created_at, last_updated_at) 
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (id, name, position, salary, created_at, last_updated_at))
    
    conn.commit() 
    response={}
    response['msg']='post successful'
    response['data']=data
    print(response)
    
    cur.close()
    conn.close()
    
    return response

if __name__ == "__main__":
    app.run(debug=False)
