# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:38:26 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:27:52 2024

@author: user
"""

from flask import Flask, render_template, request

app = Flask(__name__)

l1 = []

response = {}

@app.route('/product', methods=['POST'])
def pleaseInsert():
    print("hello......")
    data = request.get_json()
    print(data)
    l1.append(data)
    response['msg'] = "Inserted the data"
    response['data'] = l1
    return response

@app.route('/product', methods=['GET'])
def pleaseGet():
    return "I have got it"

if __name__ == '__main__':
    app.run(debug=False)
