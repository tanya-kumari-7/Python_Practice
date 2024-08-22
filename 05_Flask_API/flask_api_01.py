# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:27:52 2024

@author: user
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    return "Hello, Flask!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=False)
