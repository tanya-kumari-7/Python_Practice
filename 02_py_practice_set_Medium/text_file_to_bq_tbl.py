import os
from google.cloud import bigquery

# Set credentials
file_path = r"C:\Users\Admin\Downloads\mydb_connection.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path

# Initialize client
client = bigquery.Client()

# Local text file (CSV-like format assumed)
local_file = r"C:\Users\Admin\Downloads\sample.txt"

# Target BQ details
project_id = "mydb-470314"
dataset_id = "z_tanya"
table_id = "txt_file_table"

# Define full table path
table_ref = f"{project_id}.{dataset_id}.{table_id}"

# Configure job - let BigQuery autodetect schema
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,  # or NEWLINE_DELIMITED_JSON if JSON file
    skip_leading_rows=1,                     # if first row is header
    autodetect=True
)

# Open file and upload
with open(local_file, "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_ref,
        job_config=job_config
    )  

print("Starting job:", load_job.job_id)
load_job.result()  # Wait for the job to complete

# Confirm table schema
table = client.get_table(table_ref)
print("Table created:", table.full_table_id)
print("Schema:", [(schema.name, schema.field_type) for schema in table.schema])

#############33
