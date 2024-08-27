import pandas as pd
import psycopg2

postgres={
    'dbname':'mydatabase',
    'user':'postgres',
    'password':'Jaimatadi@123',
    'host':'localhost',
    'port':'5432'
    }

conn=psycopg2.connect(** postgres)
cur=conn.cursor()
cur.execute('''
             select * from t_emp
             ''')
data = pd.DataFrame(cur.fetchall())
data.columns = [desc[0] for desc in cur.description]  # Set column names
cur.close()
conn.close()
print(data)
 