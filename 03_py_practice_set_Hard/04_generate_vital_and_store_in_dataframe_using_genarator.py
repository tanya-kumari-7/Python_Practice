# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:33:53 2024

@author: user
"""
import random
import pandas as pd


## Data Generation
def generate_vital():
    vital_df = pd.DataFrame()
    
    for x in range(1,11):  
        vital = {}
        vital['patient_id'] = x
        vital['hr'] = random.randint(60, 90)
        vital['rr'] = random.randint(30, 50)
        vital['spo2'] = random.randint(95, 105)
        df1 = pd.DataFrame([vital])
        vital_df = pd.concat([vital_df, df1],ignore_index=True)
    return vital_df

## Outlier : - 
## if HR rate is more than 85 :- replace it with 65
## if RR rate is more than 45 and less than 35 :- replace it with 40
## if SP02 rate is less than 97 :- replace it with 99
#vital_df['hr'] = vital_df[vital_df['hr'] > 85]

## Handling oulier for HR
def hr_outlier(vital_df):
    holder = []
    for x in vital_df['hr'] :
        if x > 85:
            print('detected outlier for HR')
            holder.append(65)
        else:
            holder.append(x)
    print(holder)
    vital_df['hr'] = holder
    return vital_df

## Handling oulier for RR
def rr_outlier(vital_df):
    holder = []
    for x in vital_df['rr'] :
        if x > 45 or x < 35:
            print('detected outlier for RR')
            holder.append(40)
        else:
            holder.append(x)
    print(holder)
    vital_df['rr'] = holder
    return vital_df

## Handling oulier for HR
def spo2_outlier(vital_df):
    holder = []
    for x in vital_df['spo2'] :
        if x < 97:
            print('detected outlier for spo2')
            holder.append(99)
        else:
            holder.append(x)
    print(holder)
    vital_df['spo2'] = holder
    return vital_df


df = generate_vital()
df = hr_outlier(df)
df = rr_outlier(df)
df = spo2_outlier(df)


## Create ouput as one df for each patient

def createDfAndSave():
    for x in df['patient_id'].unique():
        df_name = f'df_{x}' 
        df_name = df[df['patient_id'] == x]
        patientid = df_name.iloc[0]['patient_id']
        df_name.to_csv(f'{patientid}.csv')
        
createDfAndSave()


















    

    
    
    