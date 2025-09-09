from flask import Flask,request,jsonify
from google.cloud import bigquery
import pandas as pd

app = Flask(__name__)
client = bigquery.Client.from_service_account_json(r"C:/Users/Admin/Downloads.My workflow.json")

# connecting to bigquery
PROJECT_ID = "mydb-470314"
DATASET_ID = "z_tanya"
TABLE_ID = "vle_master"
TABLE_REF = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"


app.route('/create',methods=['POST'])
def create_record():
    data = request.json
    errors = client.insert_rows_json(TABLE_REF,[data])

    if errors:
        return jsonify({"errors":errors}),400
    
    return jsonify({"message": "Record inserted successfully"}), 201


