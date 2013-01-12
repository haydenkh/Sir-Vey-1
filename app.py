from flask import Flask
from flask import request, render_template, url_for, redirect, flash

import db


app = Flask(__name__)
app.secret_key = 'oyeah'


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("test-create2.html")

    else:
        
       question = request.form['question']
       qtype = request.form['qtype']
       length = request.form['length']
       
       #if anon isn't checked set to null
       try:
           anon = request.form['anon']
       except:
           anon = ''
       #set answers null incase text
       answers = []

       i = 1
       if qtype =='mc':
           #iterate through answers written depending on length
           while(i < int(length) + 1):
               answer = request.form['Answer%d' %i]
               answers.append(str(answer))
               i = i+1
       #save form        
       db.add_form(question,qtype,answers,anon)
       
       return redirect(url_for('create_form',question=question))
        
        
@app.route("/form")
@app.route("/form/<question>", methods = ['POST','GET'])
def create_form(question=None):
    #get questions variables here and use them
    if request.method == "GET":
        return render_template("created-form.html",question=question,qtype=db.get_qtype(question),answers=db.get_answers(question))

        



if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
