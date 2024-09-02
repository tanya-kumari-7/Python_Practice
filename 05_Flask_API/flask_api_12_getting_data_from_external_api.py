import requests
import pandas as pd
from pandas import json_normalize

api='https://instagram243.p.rapidapi.com/searchlocation/paris'
headers={
    'x-rapidapi-host': 'instagram243.p.rapidapi.com',
    'x-rapidapi-key':'236468e9a5msh539c0273f05d5a9p1d157cjsn0ad96f67d2f2'
    }

response= requests.get(api,headers=headers)
data=response.json()
print(data)
df = json_normalize(data.get('data'))


