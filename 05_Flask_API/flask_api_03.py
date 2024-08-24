# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:09:23 2024

@author: user
"""


from flask import Flask, render_template, request

# ~POST API

app= Flask(__name__)
response={}
@app.route('/',methods=['GET'])
def addAPI():
    request_json= request.get_json()
    print(request_json.get("a"))
    print(request_json.get("b"))    
    sum=request_json.get("a") + request_json.get("b")
   
    response['msg']= 'Add data'
    response['data']=sum
    return response


if __name__ == '__main__':
    app.run(debug=False)

    