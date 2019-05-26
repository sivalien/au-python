#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="img", static_url_path="", template_folder="templates")

import math

def is_simple(value: 'int') -> 'bool':
    if value == 1:
        return False
    for i in range (2, int(math.sqrt(value)) + 2) :
        if value % i == 0 and value != i :
            return False
    return True

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/is_simple', methods = ['GET'])
def hello_name():
    if request.method == 'GET':
        num_param=request.args.get('num')
    

    b = False
    if num_param==None:
        num_param='0'
        b = True

    if not b:
        if is_simple(int(num_param)):
            res = "The number is simple"
        else:
            res = "The number isn't simple"
    else:
        res = 'Enter the number, please'

    return flask.render_template(
        'is_simple.html',
        is_simple=res
    )

if __name__ == '__main__':
   app.run(debug = True)
