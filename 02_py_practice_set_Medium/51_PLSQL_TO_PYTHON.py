import psycopg2
import pandas as pd

conn=psycopg2.connect(
    dbname='mydatabase',
    user='postgres',
    password='Jaimatadi@123',
    host='localhost',
    port=5432
    )
curr=conn.cursor()
query=curr.execute(''' select * from t_emp''')
df=pd.DataFrame(curr.fetchall())
print(df)

conn.close()
curr.close()
