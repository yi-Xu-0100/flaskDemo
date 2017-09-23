# -*- coding:utf-8 -*- 
"""
fileName: hello.py
Created Time: 2017年09月22日 星期五 21时28分59秒
description:
"""

__author__ = 'yi_Xu'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
