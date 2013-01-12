from flask import Flask
from flask import request, render_template, url_for, redirect, flash

import db


app = Flask(__name__)
app.secret_key = 'oyeah'

user ="Eliftw@gmail.com"

@app.route("/", methods = ['GET', 'POST'])
def create_form():
    
    
    if request.method == 'GET':
        if user == "Eliftw@gmail.com":
            return render_template("test-create2.html")
        else:
            return render_template("profile.html")
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
       
       return redirect(url_for('take_survey',question=question))
        
        
@app.route("/form")
@app.route("/form/<question>", methods = ['POST','GET'])
def take_survey(question=None):
    #get questions variables here and use them
    if request.method == "GET":
        return render_template("created-form.html",
                               question=question,
                               qtype=db.get_qtype(question),
                               answers=db.get_answers(question))


@app.route("/user")
@app.route("/user/<user>",methods = ['POST','GET'])
def profile_page():
    if request.method == "GET":
        tmp = db.get_recipient_answerids(user)
        forms = []
        for i in tmp:
            forms.append(db.get_question_r(i))
        forms = ["asada","ellie","asdasd"]
        return render_template("profile.html",
                               user = user,
                               form_ids = forms)

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
