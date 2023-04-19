from flask import Flask, request
import math

app = Flask(__name__)


@app.route('/lebo1/', methods=['POST'])
def lebo1():
    if 'dog' in request.json and 'years' in request.json:
        n = request.json['n']
        if n == 1:
            return {'n': 14, 'units': 'years', 'type': 'human'}
        if n == 1.5:
            return {'n': 20, 'units': 'years', 'type': 'human'}
        if n == 2:
            return {'n': 24, 'units': 'years', 'type': 'human'}
        if n == 3:
            return {'n': 30, 'units': 'years', 'type': 'human'}
        if n == 4:
            return {'n': 36, 'units': 'years', 'type': 'human'}
        if n == 5:
            return {'n': 40, 'units': 'years', 'type': 'human'}
        if n == 6:
            return {'n': 42, 'units': 'years', 'type': 'human'}
        if n == 7:
            return {'n': 49, 'units': 'years', 'type': 'human'}
        if n == 8:
            return {'n': 56, 'units': 'years', 'type': 'human'}
        if n == 9:
            return {'n': 63, 'units': 'years', 'type': 'human'}
        if n == 10:
            return {'n': 65, 'units': 'years', 'type': 'human'}
        if n == 11:
            return {'n': 71, 'units': 'years', 'type': 'human'}
        if n == 12:
            return {'n': 75, 'units': 'years', 'type': 'human'}
    if 'dog' in request.json and 'month' in request.json:
        n = request.json['n']
        if n == 2:
            return {'n': 14, 'units': 'month', 'type': 'human'}
        if n == 6:
            return {'n': 5, 'units': 'years', 'type': 'human'}
        if n == 8:
            return {'n': 9, 'units': 'years', 'type': 'human'}

    if 'human' in request.json and 'years' in request.json:
        n = request.json['n']
        if n == 5:
            return {'n': 6, 'units': 'month', 'type': 'dog'}
        if n == 9:
            return {'n': 8, 'units': 'month', 'type': 'dog'}
        if n == 14:
            return {'n': 1, 'units': 'years', 'type': 'dog'}
        if n == 20:
            return {'n': 1.5, 'units': 'years', 'type': 'dog'}
        if n == 24:
            return {'n': 2, 'units': 'years', 'type': 'dog'}
        if n == 30:
            return {'n': 3, 'units': 'years', 'type': 'dog'}
        if n == 36:
            return {'n': 4, 'units': 'years', 'type': 'dog'}
        if n == 40:
            return {'n': 5, 'units': 'years', 'type': 'dog'}
        if n == 42:
            return {'n': 6, 'units': 'years', 'type': 'dog'}
        if n == 49:
            return {'n': 7, 'units': 'years', 'type': 'dog'}
        if n == 56:
            return {'n': 8, 'units': 'years', 'type': 'dog'}
        if n == 63:
            return {'n': 9, 'units': 'years', 'type': 'dog'}
        if n == 65:
            return {'n': 10, 'units': 'years', 'type': 'dog'}
        if n == 71:
            return {'n': 11, 'units': 'years', 'type': 'dog'}
        if n == 75:
            return {'n': 12, 'units': 'years', 'type': 'dog'}
    if 'human' in request.json and 'month' in request.json:
        n = request.json['n']
        if n == 14:
            return {'n': 2, 'units': 'month', 'type': 'dog'}
    return {'n': 2, 'units': 'month', 'type': 'dog'}


app.run(host='0.0.0.0', port=5000)
