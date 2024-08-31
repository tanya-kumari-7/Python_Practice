import psycopg2
import pandas as pd
from flask import Flask
import requests

postgres = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'Jaimatadi@123',
    'host': 'localhost',
    'port': '5432'
}

url='https://yahoo-finance15.p.rapidapi.com/api/v1/markets/options/most-active?type=STOCKS'

app = Flask(__name__)
@app.route('/stock', methods=['POST'])

def POST_api():
    conn=psycopg2.connect(** postgres)
    cur=conn.cursor()
    
    # Example of calling an external API
    api_url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/options/most-active?type=STOCKS'  # Replace with the actual API URL
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com',
               'x-rapidapi-key': '236468e9a5msh539c0273f05d5a9p1d157cjsn0ad96f67d2f2'}  # Replace with your API key if needed

    # Send a POST request to the external API
    response = requests.get(api_url,  headers=headers)
    data = response.json()
    print(response.json())
    
    org_data = pd.DataFrame(data["body"])

    for index, row in org_data.iterrows():
        symbol = row.get("symbol")
        symbolType = row.get("symbolType")
        symbolName = row.get("symbolName")
        hasOptions = str(row.get("hasOptions"))
        lastPrice = str(row.get("lastPrice"))
        priceChange = str(row.get("priceChange"))
        percentChange = str(row.get("percentChange"))
        optionsImpliedVolatilityRank1y =str( row.get("optionsImpliedVolatilityRank1y"))
        optionsTotalVolume = str(row.get("optionsTotalVolume"))
        optionsPutVolumePercent = str(row.get("optionsPutVolumePercent"))
        optionsCallVolumePercent = str(row.get("optionsCallVolumePercent"))
        optionsPutCallVolumeRatio = str(row.get("optionsPutCallVolumeRatio"))
        tradeTime = row.get("tradeTime")
        symbolCode = row.get("symbolCode")
        print(f'symbol :{symbol} symbolType: {symbolType} lastPrice : {lastPrice}')
        query = '''
        INSERT INTO stock_tbl_get_api 
        ("symbol", "symboltype", "symbolname", "lastprice", "pricechange",
         "percentchange", "optionsimpliedvolatilityrank1y", "optionstotalvolume", "optionsputvolumepercent",
         "optionscallvolumepercent", "optionsputcallvolumeratio", "tradetime", "symbolcode")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

        cur.execute(query, (symbol, symbolType, symbolName, lastPrice, priceChange, percentChange, optionsImpliedVolatilityRank1y, optionsTotalVolume, optionsPutVolumePercent, optionsCallVolumePercent, optionsPutCallVolumeRatio, tradeTime, symbolCode))

    
        conn.commit()
    response={}
    response['msg']='post successful'
    response['data']=data
    print(response)
    
    cur.close()
    conn.close()
    
    return response

app.run(debug=False)
    
    
    
    

            
 
    
    

