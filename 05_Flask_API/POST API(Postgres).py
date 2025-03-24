from flask import Flask, request, jsonify
import pandas as pd
import psycopg2


postgres = {
    'dbname':'mydatabase',
    'user' : 'postgres',
    'password':'Jaimatadi@123',
    'host':'localhost',
    'port' : 5432
    }

app = Flask(__name__)
@app.route("/user_registration", methods=['POST'])

def post_api():
    conn = psycopg2.connect(**postgres)
    curr = conn.cursor()
    
    data = request.get_json()
    user_name = data.get('user_name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    city = data.get('city')
    
    print(user_name,email,password,role,city)
    
    curr.execute('''
        INSERT INTO public.api_users_table (user_name,email,password,role,city)
        VALUES (%s,%s,%s,%s,%s)
        ''',(user_name,email,password,role,city))
    
    
    response = {}
    response['msg'] = 'Registration Successfuly Completed'
    response['data'] = data
    print(response)
    
    curr.close()
    #conn.commit
    conn.close()
    return response

if __name__ == "__main__":
    app.run(debug=False)
    
   
