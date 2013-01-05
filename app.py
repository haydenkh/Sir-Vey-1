from flask import Flask
from flask import request, render_template, url_for, redirect, flash


app = Flask(__name__)
app.secret_key = 'oyeah'


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("test-create.html")
    else:
        question = request.form['question']
        qtype = request.form['qtype']
        length = request.form['length']
        
        
