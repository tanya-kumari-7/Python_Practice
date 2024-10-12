#Createing CSV ##############################################################################
"""
Generate students data and export it into a CSV file.
"""

import pandas as pd
import random

# create a blank dataframe
student_master=pd.DataFrame(columns=["student_Id","student_name","school_name","grade","parent_contact","age"])
type(student_master)

# generate data for students

temp_student_list =[]
for x in range (1,11):
    for y in range(1,(x*10)+1):
        student_Id = f"GGPS_class{x}_{y}"
        school_name = "GGPS"
        grade = ["A", "B", "C", "D", "F"]
        first_names = ["John", "Jane", "Sam", "Sara", "Alex", "Emily", "Daniel", "Sophia", "Michael", "Olivia","test"]
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
        temp_student_list.append({
            "student_Id":student_Id,
            "student_name" : f"{random.choice(first_names)} {random.choice(last_names)}",
            "school_name":school_name,
            "grade" : random.choice(grade),
            "parent_contact" : f"{random.randint(6,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}",
            "age" : f"{random.randint(16,20)}"
            })

student_master=pd.DataFrame(temp_student_list)
student_master.to_csv(r"C:\Users\user\Documents\student_data.csv", index=False)
        

#Reading CSV ##############################################################################


"""
Read_CSV_and_create_bronze_layer_postgres_table 
"""

import pandas as pd
import psycopg2

# connecting to postgres

data = pd.read_csv(r"C:\Users\user\Documents\student_data.csv")
postgres={
    'dbname':'mydatabase',
    'user':'postgres',
    'password':'Jaimatadi@123',
    'host':'localhost',
    'port':'5432'
    }

try:
    conn=psycopg2.connect(**postgres)
    cur=conn.cursor()
    for index, row in data.iterrows():
        cur.execute(
            """
            INSERT INTO student_master_bronze (student_Id, student_name,school_name,grade,parent_contact,age)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,(row["student_Id"],row["student_name"],row["school_name"],row["grade"],row["parent_contact"],row["age"])
            )
        conn.commit()
    
    
except Exception as e:
    print(e)
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()