#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    return 'c {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_is(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if n % 2 == 1:
        string = "{} is odd".format(n)
    else:
        string = "{} is even".format(n)
    return render_template('6-number_odd_or_even.html', string=string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
