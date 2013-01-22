from pymongo import Connection
from bson.objectid import ObjectId

Connection = Connection('mongo.stuycs.org')

def drop_collection2():
    collection = connect2()
    collection.drop()

def drop_collection1():
    collection = connect1()
    collection.drop()

def connect1():
    #Connects and Authenticates
    #this collection is for forms
    DB = Connection.admin
    res = DB.authenticate('ml7','ml7')
    DB = Connection['z-pd7-SirVey']
    collection = DB.collection1
    return collection

def connect2():
    #Connects and Authenticates                                        
    #this collection is for the results
    DB = Connection.admin
    res = DB.authenticate('ml7','ml7')
    DB = Connection['z-pd7-SirVey']
    collection = DB.collection2
    return collection



def add_form(question,qtype,answers,anon,correct):
    #str question
    #str qtype
    #array answers
    #boolean anon
    collection = connect1()
    if(collection.find({'question':question}).count() > 0):
        return False
    else:
        d = {'question':question,'qtype':qtype,'answers':answers,'anon':anon,'correct':correct}
        collection.insert(d)
        return True

def get_anon(question):
    #returns anon as a bool
    collection = connect1()
    anon = [x for x in collection.find({'question':question})]
    if len(anon) != 1:
        return
    anon = anon[0]
    anon = anon['anon']
    return anon

def get_answers(question):
    #Returns the answer for question
    collection = connect1()
    answer = [x for x in collection.find({'question':question})]
    if len(answer) != 1:
        return
    answer = answer[0]
    answer = answer['answers']
    return answer


def get_qtype(question):
    #Returns the qtype for question
    collection = connect1()
    qtype = [x for x in collection.find({'question':question})]
    if len(qtype) != 1:
        return
    qtype = qtype[0]
    qtype = qtype['qtype']
    return qtype
    

def get_question_id(question):
    #Return question ID
    collection = connect1()
    r = [i for i in collection.find({'question':question})]
    if len(r) == 0:
        return
    questionid = r[0]
    return questionid['_id']

def get_question(questionid):
    collection = connect1()
    question =  [i for i in collection.find({'_id':ObjectId(questionid)})]
    if len(question) ==0:
        return
    question = question[0]
    return question['question']

def get_forms():
    #return's forms by question
    collection = connect1()
    forms = []
    res = collection.find()
    for i in res:
        forms.append(str(i['question']))
        
    return forms

#################################################
########## START OF RESULT METHODS ##############
#################################################

def send_question(question,recipient):
    #send questions to list of recipients
    #later they will fill in the answer
    collection = connect2()
    for i in recipient: 
        if collection.find({'question':question,
                            'recipient':i}).count() == 0:

            d = {'question':question,'recipient':i,'answer':[]}
            collection.insert(d)
    

def get_answer_id(question,recipient):
    collection = connect2()
    answerid = [i for i in collection.find({'question':question,'recipient':recipient})]
    if len(answerid) == 0:
        return
    else:
        answerid = answerid[0]
        return answerid['_id']

def get_results():
    #return the _id of all results 
    collection = connect2()
    results = []
    res = collection.find()
    results =[x['_id'] for x in res]
    return results


def get_answer(answerid):
    #returns the selected answer for a given result id
    collection = connect2()
    answer =  [i for i in collection.find({'_id':ObjectId(answerid)})]
    if len(answer) == 0:
        return
    answer = answer[0]
    return answer['answer']


def get_recipient(answerid):
    #get recipient by id
    collection = connect2()
    recipient = [i for i in collection.find({'_id':ObjectId(answerid)})]
    if len(recipient) == 0:
        return
    recipient = recipient[0]
    return  recipient['recipient']


def get_question_r(answerid):
    #returns question based on answer id
    collection = connect2()
    question = [i for i in collection.find({'_id':answerid})]
    if len(question) != 1:
        return
    question = question[0]
    question = question['question']
    return question

def get_recipient_answerids(recipient):
    #returns answer id's associated with recipient
    collection = connect2()
    answerid = []
    r = [i for i in collection.find({'recipient':recipient})]
    
    if len(r) == 0:
        print "r=0"
        return

    for i in r:
        answerid.append(i['_id'])
    return answerid
    
def set_answer(answerid, answer):
    collection = connect2()
    d = [x for x in collection.find({'_id':ObjectId(answerid)})]
    if len(d) == 0:
        return
    d = d[0]
    print d
    tmp =  d['answer']
    print tmp
    tmp.append(answer)
    collection.update({'_id':ObjectId(answerid)},d)


def get_recipient_answers(recipient):
    answers = []
    answerids = get_recipient_answerids(recipient)
    for i in answerids:
        answers.append(get_answer(i))
    return answers

def get_recipient_questions(recipient):        
    questions = []
    answerids = get_recipient_answerids(recipient)
    for i in answerids:
        questions.append(get_question_r(i))
    return questions
