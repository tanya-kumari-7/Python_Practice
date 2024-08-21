# =============================================================================
'''
Write a Pandas program to split the following dataframe into groups,
group by month and year based on order date and find the total purchase amount year wise, month wise.

'''
# =============================================================================
import pandas as pd

orders_data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2015-08-17','2012-09-10',
            '2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]
})

orders_data['ord_month']=pd.to_datetime(orders_data['ord_date']).dt.month
orders_data['ord_year']=pd.to_datetime(orders_data['ord_date']).dt.year
orders_data['ord_month_year']=pd.to_datetime(orders_data['ord_date']).dt.strftime('%b %Y')

resulr=orders_data.groupby(['ord_year','ord_month']).agg({'purch_amt':'sum'})

