import os
import re
import pandas as pd
from google.cloud import bigquery
from google.api_core import retry
import logging

# -----------------------
# 1. Setup Logging
# -----------------------
logging.basicConfig(
    filename='upload_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -----------------------
# 2. Google Credentials
# -----------------------
file_path = r"C:\Users\Admin\Downloads\mydb_connection.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path

# -----------------------
# 3. Read and Validate TXT File
# -----------------------
local_file = r"C:\Users\Admin\Downloads\client_master_test.txt"

# Read header row to get column names
try:
    df_headers = pd.read_csv(local_file, sep="|", nrows=0, dtype=str)
    logger.info(f"Headers read successfully: {list(df_headers.columns)}")
except Exception as e:
    logger.error(f"Error reading headers: {str(e)}")
    raise

# -----------------------
# 4. Clean Column Names for BigQuery
# -----------------------
def clean_bq_column(col: str) -> str:
    col = col.strip()
    col = col.replace(" ", "_").replace("/", "_").replace(".", "_")
    col = re.sub(r"[^a-zA-Z0-9_]", "", col)
    if col and col[0].isdigit():
        col = "_" + col
    return col

clean_columns = [clean_bq_column(c) for c in df_headers.columns]
column_mapping = dict(zip(df_headers.columns, clean_columns))

logger.info("\n=== Column Mapping (Original → Cleaned) ===")
for orig, clean in column_mapping.items():
    if orig != clean:
        logger.info(f"{orig}  -->  {clean}")

# Build BigQuery schema (all STRING)
schema = [bigquery.SchemaField(col, "STRING") for col in clean_columns]

# -----------------------
# 5. Preprocess Text File
# -----------------------
def preprocess_text_file(input_file: str, output_file: str, expected_columns: int):
    """Preprocess the text file to handle formatting issues and log problems."""
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        header_written = False
        for i, line in enumerate(infile, 1):
            # Split line by delimiter
            fields = line.strip().split("|")
            if i == 1:
                # Write header as-is (already handled by pandas)
                outfile.write(line)
                header_written = True
                continue
            # Check if row has correct number of columns
            if len(fields) != expected_columns:
                logger.warning(f"Row {i} has {len(fields)} fields, expected {expected_columns}. Adjusting...")
                # Pad with empty strings if too few fields
                if len(fields) < expected_columns:
                    fields.extend([""] * (expected_columns - len(fields)))
                # Truncate if too many fields
                fields = fields[:expected_columns]
            # Write cleaned row
            outfile.write("|".join(fields) + "\n")
    logger.info(f"Preprocessed file written to: {output_file}")

# Create a temporary cleaned file
cleaned_file = local_file.replace(".txt", "_cleaned.txt")
preprocess_text_file(local_file, cleaned_file, len(clean_columns))

# -----------------------
# 6. Upload to BigQuery
# -----------------------
client = bigquery.Client()

project_id = "mydb-470314"
dataset_id = "z_tanya"
table_id = "client_master_test"
table_ref = f"{project_id}.{dataset_id}.{table_id}"

# Load job configuration
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    field_delimiter="|",
    skip_leading_rows=1,  # Skip header
    schema=schema,
    ignore_unknown_values=True,  # Ignore extra columns
    allow_quoted_newlines=True,
    quote_character=None,
    max_bad_records=10000,  # Increase to allow more bad rows
    write_disposition="WRITE_TRUNCATE"
)

# Upload with retry logic
@retry.Retry(predicate=retry.if_exception_type(Exception), deadline=300)
def upload_to_bigquery():
    with open(cleaned_file, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            table_ref,
            job_config=job_config
        )
    logger.info(f"Starting job: {load_job.job_id}")
    load_job.result()  # Wait for completion
    return load_job

try:
    load_job = upload_to_bigquery()
except Exception as e:
    logger.error(f"Upload failed: {str(e)}")
    raise

# -----------------------
# 7. Confirm Table
# -----------------------
table = client.get_table(table_ref)
logger.info(f"Table created: {table.full_table_id}")
logger.info(f"Schema: {[(schema.name, schema.field_type) for schema in table.schema]}")
print(f"Upload complete. Check upload_log.txt for details.")