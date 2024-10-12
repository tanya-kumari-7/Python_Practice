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
        
    
        

    