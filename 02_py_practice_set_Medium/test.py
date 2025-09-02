import os
from google.cloud import bigquery
import pandas as pd
from pandasql import sqldf

file_path = r'C:\Users\Admin\Downloads\mydb_connection.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path

client = bigquery.Client()
query = "SELECT * FROM `mydb-470314.z_tanya.vle_master` LIMIT 5"
df = client.query(query).to_dataframe()

print(df.head())



