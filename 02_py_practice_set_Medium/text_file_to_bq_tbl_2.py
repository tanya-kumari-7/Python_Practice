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




# ==============================
# 3. Define fixed required columns
# ==============================
required_columns = [
   "Member Code", "Client Code", "Primary Holder First Name", "Primary Holder Middle Name", "Primary Holder Last Name", "Tax Status", "Gender", "Primary Holder DOB/Incorporation", "Occupation Code", "Holding Nature", "Second Holder First Name", "Second Holder Middle Name", "Second Holder Last Name", "Third Holder First Name", "Third Holder Middle Name", "Third Holder Last Name", "Second Holder DOB", "Third Holder DOB", "Guardian First Name", "Guardian Middle Name", "Guardian Last Name", "Guardian DOB", "Primary Holder PAN Exempt", "Second Holder PAN Exempt", "Third Holder PAN Exempt", "Guardian PAN Exempt", "Primary Holder PAN", "Second Holder PAN", "Third Holder PAN", "Guardian PAN", "Primary Holder-Exempt Category", "Second Holder Exempt Category", "Third Holder Exempt Category", "Guardian Exempt Category", "Client Type", "PMS", "Default DP", "CDSL DPID", "CDSLCLTID", "CMBP Id", "NSDLDPID", "NSDLCLTID", "Account Type 1", "Account No 1", "MICR No 1", "IFSC Code 1", "Bank Name 1", "Bank Branch 1", "Default Bank Flag 1", "Bank1 Created At", "Bank1 Last Modified At", "Bank1 Status", "Account Type 2", "Account No 2", "MICR No 2", "IFSC Code 2", "Bank Name 2", "Bank Branch 2", "Default Bank Flag 2", "Bank2 Created At", "Bank2 Last Modified At", "Bank2 Status", "Account type 3", "Account No 3", "MICR No 3", "IFSC Code 3", "Bank Name 3", "Bank Branch 3", "Default Bank Flag 3", "Bank3 Created At", "Bank3 Last Modified At", "Bank3 Status", "Account type 4", "Account No 4", "MICR No 4", "IFSC Code 4", "Bank Name 4", "Bank Branch 4", "Default Bank Flag 4", "Bank4 Created At", "Bank4 Last Modified At", "Bank4 Status", "Account type 5", "Account No 5", "MICR No 5", "IFSC Code 5", "Bank Name 5", "Bank Branch 5", "Default Bank Flag 5", "Bank5 Created At", "Bank5 Last Modified At", "Bank5 Status", "Cheque Name", "Div pay mode", "Address 1", "Address 2", "Address 3", "City", "State", "Pincode", "Country", "Resi. Phone", "Resi. Fax", "Office Phone", "Office Fax", "Email", "Communication Mode", "Foreign Address 1", "Foreign Address 2", "Foreign Address 3", "Foreign Address City", "Foreign Address Pincode", "Foreign Address State", "Foreign Address Country", "Foreign Address Resi Phone", "Foreign Address Fax", "Foreign Address Off. Phone", "Foreign Address Off. Fax", "Indian Mobile No.", "Primary Holder KYC Type", "Primary Holder CKYC Number", "Second Holder KYC Type", "Second Holder CKYC Number", "Third Holder KYC Type", "Third Holder CKYC Number", "Guardian KYC Type", "Guardian CKYC Number", "Primary Holder KRA Exempt Ref. No.", "Second Holder KRA Exempt Ref. No.", "Third Holder KRA Exempt Ref. No", "Guardian Exempt Ref. No", "Aadhaar Updated", "Mapin Id.", "Paperless_flag", "LEI No", "LEI Validity", "Email Declaration Flag", "Mobile Declaration Flag", "Branch", "Dealer", "Nomination Opt", "Nomination Authentication Mode", "Nominee 1 Name", "Nominee 1 Relationship", "Nominee 1 Applicable(%)", "Nominee 1 Minor Flag", "Nominee 1 DOB", "Nominee 1 Guardian", "Nominee 1 Guardian PAN", "NOM1_ID_TYP", "NOM1_IDNO", "NOM1_EMAIL", "NOM1_MOB", "NOM1_ADD1", "NOM1_ADD2", "NOM1_ADD3", "NOM1_CITY", "NOM1_PIN", "NOM1_CON", "Nominee 2 Name", "Nominee 2 Relationship", "Nominee 2 Applicable(%)", "Nominee 2 DOB", "Nominee 2 Minor Flag", "Nominee 2 Guardian", "Nominee 2 Guardian PAN", "NOM2_ID_TYP", "NOM2_IDNO", "NOM2_EMAIL", "NOM2_MOB", "NOM2_ADD1", "NOM2_ADD2", "NOM2_ADD3", "NOM2_CITY", "NOM2_PIN", "NOM2_CON", "Nominee 3 Name", "Nominee 3 Relationship", "Nominee 3 Applicable(%)", "Nominee 3 DOB", "Nominee3 Minor Flag", "Nominee3 Guardian", "Nominee 3 Guardian PAN", "NOM3_ID_TYP", "NOM3_IDNO", "NOM3_EMAIL", "NOM3_MOB", "NOM3_ADD1", "NOM3_ADD2", "NOM3_ADD3", "NOM3_CITY", "NOM3_PIN", "NOM3_CON", "NOM_SOA", "Second Holder Email", "Second holder Email Declaration", "Second holder Mobile", "Second holder Mobile Declaration", "Third Holder Email", "Third holder Email Declaration", "Third holder Mobile", "Third holder Mobile Declaration", "Nomination Flag", "Nomination Authentication Date", "Guardian Relationship", "Created By", "Created At", "Last Modified By", "Last Modified At"
]
# Read file (pipe separated)
# df = pd.read_csv(local_file, sep="|")
# df = pd.read_csv(local_file, sep="|", on_bad_lines="skip", engine="python")
df = pd.read_csv(local_file, delimiter="|", dtype=str)

# Keep only required columns (drop extra ones)
df = df[[col for col in required_columns if col in df.columns]]

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
