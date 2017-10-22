import flask
from flask import render_template
from flask import request
import json
import sys
import add.py

app = flask.Flask(__name__)
sums = []

@app.route('/', methods = ["GET", "POST"])
def homePage():
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")
    sum = add(num1,num2)
    sums = addNum(sum,sums)
    return render_template("calc.html")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
