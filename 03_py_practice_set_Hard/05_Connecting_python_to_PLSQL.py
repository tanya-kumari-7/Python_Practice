

import psycopg2
import pandas as pd

def fetch_data():
    try:
        # Establishing the connection
        conn = psycopg2.connect(
            dbname='mydatabase',
            user='postgres',
            password='Jaimatadi@123',
            host='localhost',
            port='5432'
        )
        
        # Creating a cursor object
        curr = conn.cursor()
        
        # Executing the SQL query
        curr.execute('SELECT * FROM t_emp')
        
        # Fetching all rows from the executed query
        data = curr.fetchall()
        
        # Converting the data into a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Displaying DataFrame information
        print(df)
        
        # Closing the cursor and connection
        curr.close()
        conn.close()
        
    except psycopg2.Error as e:
        print(f"Failed to connect to the database: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data()
