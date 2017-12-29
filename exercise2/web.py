#keep fields filled after returns happen
#error handling
#push all to github

from flask import Flask, render_template, request
from modtest import evenDivisors
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/process", methods=['POST'])
def process():
    min = int(request.form['min'])
    max = int(request.form['max'])
    divisor = int(request.form['divisor'])
    data = evenDivisors(min, max, divisor)
    return render_template('index.html', data=data, min=min, max=max, divisor=divisor)