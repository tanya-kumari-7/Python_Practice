from flask import Flask,request,jsonify
from google.cloud import bigquery
import pandas as pd

app = Flask(__name__)
client = bigquery.Client.from_service_account_json(r"C:/Users/Admin/Downloads.My workflow.json")

PROJECT_ID = "your_project_id"
DATASET_ID = "your_dataset"
TABLE_ID = "your_table"
TABLE_REF = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"


