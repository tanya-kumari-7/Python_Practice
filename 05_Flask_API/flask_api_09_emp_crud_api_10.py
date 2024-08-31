import psycopg2
import pandas as pd
from flask import Flask , request

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
    
    data= request.get_json()
    print(data)
    
    org_data = pd.DataFrame(data["body"])
    symbol = org_data.get("symbol")
    symbolType = org_data.get("symbolType")
    symbolName = org_data.get("symbolName")
    hasOptions = org_data.get("hasOptions")
    lastPrice = org_data.get("lastPrice")
    priceChange = org_data.get("priceChange")
    percentChange = org_data.get("percentChange")
    optionsImpliedVolatilityRank1y = org_data.get("optionsImpliedVolatilityRank1y")
    optionsTotalVolume = org_data.get("optionsTotalVolume")
    optionsPutVolumePercent = org_data.get("optionsPutVolumePercent")
    optionsCallVolumePercent = org_data.get("optionsCallVolumePercent")
    optionsPutCallVolumeRatio = org_data.get("optionsPutCallVolumeRatio")
    tradeTime = org_data.get("tradeTime")
    symbolCode = org_data.get("symbolCode")
    query = '''
    INSERT INTO stock table 
    ("symbol", "symbolType", "symbolName", "hasOptions", "lastPrice", "priceChange",
     "percentChange", "optionsImpliedVolatilityRank1y", "optionsTotalVolume", "optionsPutVolumePercent",
     "optionsCallVolumePercent", "optionsPutCallVolumeRatio", "tradeTime", "symbolCode")
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    cur.execute(query,(symbol, symbolType, symbolName, hasOptions, lastPrice, priceChange, percentChange, optionsImpliedVolatilityRank1y, optionsTotalVolume, optionsPutVolumePercent, optionsCallVolumePercent, optionsPutCallVolumeRatio, tradeTime, symbolCode))
    
    conn.commit()
    response={}
    response['msg']='post successful'
    response['data']=data
    print(response)
    
    cur.close()
    conn.close()
    
    return response

app.run(debug=False)
    
    
    
    

            
 
    
    

