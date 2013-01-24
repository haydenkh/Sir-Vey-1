from flask import Flask
from flask import request, render_template, url_for, redirect, flash,session 

import db
#import util


app = Flask(__name__)
app.secret_key = 'oyeah'



@app.route("/",methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        try:
            print request.form['login']
        except:
            print "null"
        return render_template("user.html")

    else:
        if request.form['button'] == 'Login':
            session['username'] =  request.form['login']
            print session['username']
            return redirect(url_for('profile_page'))



@app.route("/send", methods = ['GET','POST'])
def send_forms():
    if request.method == "GET":
        return render_template("director.html",
                               #Place holder for Emails.txt
                               students = ["Eliftw@gmail.com","Alex"],
                               forms = db.get_forms())

    else:
        print request.form['question']
        db.send_question(str(request.form['question']),[request.form['student']])
        return redirect(url_for('director'))



@app.route("/director",methods = ['GET','POST'])
def director():
    if request.method == "GET":
        return render_template("directorprofile.html")

    else:
        print request.form['button']
        if request.form['button'] == 'create':
            return redirect(url_for('create_form'))
        if request.form['button'] == 'send':
            return redirect(url_for('send_forms'))

    

@app.route("/create", methods = ['GET', 'POST'])
def create_form():
    
    if request.method == 'GET':
            return render_template("test-create2.html")

    else:
       print request.form['qtype']
       question = request.form['question']
       qtype = request.form['qtype']

       try:
           length = request.form['length']

       except:
           print "null"
           
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
       db.add_form(question,qtype,answers,anon,'0')
       
       return redirect(url_for('director'))
        
        
@app.route("/form")
@app.route("/form/<question>", methods = ['POST','GET'])
def take_survey(question=None):
    print "take_survey"
    #get questions variables here and use them
    if request.method == "GET":
        return render_template("created-form2.html",
                               question=question,
                               qtype=db.get_qtype(question),
                               answers=db.get_answers(question))
    else:
        answer = request.form['response']
        answerid = db.get_answer_id(question,session['username'])
        db.set_answer(answerid,answer)
        flash("Thank You!")
        return redirect(url_for("profile_page"))



@app.route("/user",methods = ['POST','GET'])
def profile_page():
    if request.method == "GET":
        #this checks the database 
        tmp = db.get_recipient_answerids(session['username'])
        forms = []
        try:
            for i in tmp:
                if db.get_answer(i) == []:
                    forms.append(db.get_question_r(i))
        except:
            print "exception"
        return render_template("userprofile.html",
                                user = session['username'],
                                form_ids = forms,
                                numquestions = 5)

    else:
        if request.form['button'] == 'take survey':
            question = request.form['question']
            print question
            return redirect(url_for('take_survey',question=question))

        if request.form['button'] == 'logout':
            return redirect(url_for('login'))

        if request.form['button'] == 'results':
            return redirect(url_for('results'))

@app.route("/results",methods = ['POST','GET'])
def results():
    if request.method == "GET":
        answers = db.get_recipient_answers(session['username'])
        questions = db.get_recipient_questions(session['username'])
        
        return render_template("results.html",
                               questions = questions,
                               answers = answers)

    else:
        return redirect(url_for('profile_page'))

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
