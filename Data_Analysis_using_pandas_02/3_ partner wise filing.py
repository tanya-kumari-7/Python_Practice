# IMPORTS
import pandas as pd
import plotly.express as px

#  Read CSV

offline_df = pd.read_csv(r"C:\Users\user\Downloads\offline_paid.csv")
offline_df.head(5)

#  EXPLORE DATA
pd.set_option('display.max_columns', None)

offline_df.head(5)

offline_df.tail(5)

offline_df.count()

offline_df.describe()

list(offline_df.columns)

offline_df.info()

print(f'Number of rows in DF is {offline_df.shape[0]} & numner of columns in DF is {offline_df.shape[1]}')

offline_df.isnull().sum()
print(offline_df.isnull().sum().to_string())

offline_df.dtypes

selected_column = ['emitra_id',
 'itr_id',
 'sp_name',
 'sso_id',
 'Payment_datetime',
 'Payment_date',
 'Merchant_first_filing_date',
 'merchant_last_filing_date',
 'merchant_created_on',
 'Gross_revenue',
 'Net_Revenue',
 'Net_Revenue_with_gst',
 'assessment_year',
 'form_name',
 'itr_status',
 'filing_Status',
 'E_verification_status',
 'Filing_type',
 'Filing_mode',
 'Age_bucket',
 'gender',
 'Latest_Business_income_band',
 'Latest_Salaried_income_band',
 'Latest_os_income_band',
 'Latest_hp_income_band',
 'Latest_capital_gain_band',
 'Gross_total_income_band',
 'total_income_band',
 'tds_refund_band',
 'Tax_payable_slabs',
 'tax_deducted_band',
 'state',
 'Tier',
 'zone',
 'contest_status',
 'Ops_category1_status',
 'Ops_category2_status',
 'Ops_category3_status',
 'team_reamrks_count',
 'User_type',
 'Vle_type',
 'Income_band',
 'FY_Year']

df = offline_df[selected_column]

df.columns.to_list()

df.head(5)

"""
WILL HANDLE NULL VALUES WHILE WORKING AS I DONT WANT TO REMOVE OR REPLACE NULL VALUES NOW
"""
df["sp_name"].count()

df["sp_name"].unique()

partner_wise_filing_count = df.groupby("sp_name")['emitra_id'].count().reset_index(name='filing_count')

# fig = px.bar(
#     partner_wise_filing_count,
#     x = 'sp_name',
#     y = 'filing_count',
#     title = 'partner wise filing'
#     )

# fig.show()

fig = px.bar(
    partner_wise_filing_count,
    x="sp_name",
    y="filing_count",
    title="Partner Wise Filing",
    text="filing_count",  # Show count on bars
    color="filing_count",  # Color bars based on count
    labels={"sp_name": "Partner Name", "filing_count": "Filing Count"},
)

fig.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels for better visibility

fig.show()

