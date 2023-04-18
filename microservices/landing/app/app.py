from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    return requests.request('GET', f'http://add-service:5050/{n1}/{n2}').json()['result']

def minus(n1, n2):
    return requests.request('GET', f'http://sub-service:5050/{n1}/{n2}').json()['result']

def multiply(n1, n2):
    return requests.request('GET', f'http://mult-service:5050/{n1}/{n2}').json()['result']

def divide(n1, n2):
    return requests.request('GET', f'http://div-service:5050/{n1}/{n2}').json()['result']

def gcd(n1, n2):
    return requests.request('GET', f'http://gcd-service:5050/{n1}/{n2}').json()['result']

def lcm(n1, n2):
    return requests.request('GET', f'http://lcm-service:5050/{n1}/{n2}').json()['result']

def exp(n1, n2):
    return requests.request('GET', f'http://exp-service:5050/{n1}/{n2}').json()['result']


@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            result = divide(number_1, number_2)
        elif operation == 'gcd':
            result = gcd(number_1, number_2)
        elif operation == 'lcm':
            result = lcm(number_1, number_2)
        elif operation == 'exp':
            result = exp(number_1, number_2)

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    except TypeError:
        flash(f'TypeError - int() arg must be string')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )