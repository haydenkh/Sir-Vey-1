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
        
       return redirect(url_for('create_form',question=question))
        
        
@app.route("/form")
@app.route("/form/<question>", methods = ['POST','GET'])
def create_form(question=None):
    #get questions variables here and use them
    if request.method == "GET":
        return render_template("created-form.html",question=question,qtype="text")

        



if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
