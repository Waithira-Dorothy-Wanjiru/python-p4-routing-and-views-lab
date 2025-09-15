#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

# ---- INDEX ROUTE ----
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# ---- PRINT STRING ----
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # prints to console
    return parameter  # plain text, no <p> tags

# ---- COUNT ----
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return "\n".join(numbers) + "\n"

# ---- MATH ----
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)  # plain text, no <p>

# ---- OPTIONAL: Request inspector (not graded) ----
@app.route('/request-info')
def request_info():
    return {
        "method": request.method,
        "url": request.url,
        "args": request.args.to_dict(),
        "headers": dict(request.headers),
    }


if __name__ == '__main__':
    app.run(port=5555, debug=True)
