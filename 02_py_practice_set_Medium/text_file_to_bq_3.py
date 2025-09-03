import os
import re
import pandas as pd
from google.cloud import bigquery

# -----------------------
# 1. Google Credentials
# -----------------------
file_path = r"C:\Users\Admin\Downloads\mydb_connection.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path

# -----------------------
# 2. Read TXT headers
# -----------------------
local_file = r"C:\Users\Admin\Downloads\client_master_test.txt"

# Read only the header row (nrows=0)
df_headers = pd.read_csv(local_file, sep="|", nrows=0, dtype=str)

# -----------------------
# 3. Clean column names
# -----------------------
def clean_bq_column(col: str) -> str:
    # Strip spaces
    col = col.strip()
    # Replace spaces, slashes, and dots with "_"
    col = col.replace(" ", "_").replace("/", "_").replace(".", "_")
    # Remove disallowed characters (only keep letters, numbers, and "_")
    col = re.sub(r"[^a-zA-Z0-9_]", "", col)
    # If starts with a digit, prepend underscore
    if col and col[0].isdigit():
        col = "_" + col
    return col

clean_columns = [clean_bq_column(c) for c in df_headers.columns]

# Keep a mapping for reference
column_mapping = dict(zip(df_headers.columns, clean_columns))

print("\n=== Column Mapping (Original → Cleaned) ===")
for orig, clean in column_mapping.items():
    if orig != clean:
        print(f"{orig}  -->  {clean}")

# Build schema: all STRING for now
schema = [bigquery.SchemaField(col, "STRING") for col in clean_columns]

# -----------------------
# 4. Upload TXT directly to BigQuery
# -----------------------
client = bigquery.Client()

project_id = "mydb-470314"
dataset_id = "z_tanya"
table_id = "client_master_test"
table_ref = f"{project_id}.{dataset_id}.{table_id}"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,   # TXT with delimiter
    field_delimiter="|",
    skip_leading_rows=1,   # skip header
    schema=schema,         # enforce sanitized schema
    ignore_unknown_values=True,
    allow_quoted_newlines=True,
    write_disposition="WRITE_TRUNCATE"  # overwrite; use WRITE_APPEND if needed
)

with open(local_file, "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_ref,
        job_config=job_config
    )

print("\nStarting job:", load_job.job_id)
load_job.result()  # wait until complete

# -----------------------
# 5. Confirm table
# -----------------------
table = client.get_table(table_ref)
print("\n✅ Table created:", table.full_table_id)
print("Schema:", [(schema.name, schema.field_type) for schema in table.schema])
