import os
import pandas as pd
from google.cloud import bigquery

# -----------------------
# 1. Google Credentials
# -----------------------
file_path = r"C:\Users\Admin\Downloads\mydb_connection.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path

# -----------------------
# 2. Read & Clean File
# -----------------------
local_file = r"C:\Users\Admin\Downloads\client_master_test.txt"

# Read file (pipe separated)
# df = pd.read_csv(local_file, sep="|")
df = pd.read_csv(local_file, sep="|", on_bad_lines="skip", engine="python")

# Clean column names
df.columns = (
    df.columns.str.strip()
              .str.replace(" ", "_", regex=False)
              .str.replace("/", "_", regex=False)
              .str.replace(".", "_", regex=False)

)

df.shape

# Save cleaned file
clean_file = r"C:\Users\Admin\Downloads\client_master_clean.txt"
df.to_csv(clean_file, sep="|", index=False)

print("Headers cleaned and file saved:", clean_file)

# -----------------------
# 3. Upload to BigQuery
# -----------------------
client = bigquery.Client()

project_id = "mydb-470314"
dataset_id = "z_tanya"
table_id = "client_master_test"
table_ref = f"{project_id}.{dataset_id}.{table_id}"

# Job config
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    field_delimiter="|",
    skip_leading_rows=1,  # first row is header
    autodetect=True,
    ignore_unknown_values=True,
    allow_quoted_newlines=True
)

# Load to BigQuery
with open(clean_file, "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_ref,
        job_config=job_config
    )

print("Starting job:", load_job.job_id)
load_job.result()  # wait for completion

# -----------------------
# 4. Confirm Table
# -----------------------
table = client.get_table(table_ref)
print("Table created:", table.full_table_id)
print("Schema:", [(schema.name, schema.field_type) for schema in table.schema])
