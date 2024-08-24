# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:09:23 2024

@author: user
"""


from flask import Flask, render_template, request

# ~POST API

app= Flask(__name__)
l1=[]
response={}
@app.route('/',methods=['GET'])
def addAPI():
    Add_date= request.get_json()
    sum_=list(Add_date.values())[0]+list(Add_date.values())[1]
    l1.append(sum_)
    response['msg']= 'Added_date'
    response['data']=l1
    return response

if __name__ == '__main__':
    app.run(debug=False)
    
    


    