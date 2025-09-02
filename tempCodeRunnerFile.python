import os
from google.cloud import bigquery
import pandas as pd
from pandasql import sqldf

file_path = r'C:\Users\user\Downloads\mydb_connection.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path

client = bigquery.Client()
query = "SELECT * FROM `bigquery-public-data.austin_crime.crime` LIMIT 10"
df = client.query(query).to_dataframe()

print(df.head())
