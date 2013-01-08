from pymongo import Connection
Connection = Connection('mongo.stuycs.org')

def connect():
    #Connects and Authenticates
    DB = Connection.admin
    res = DB.authenticate('ml7','ml7')
    DB = Connection['z-pd7-SirVey']
    collection = DB.collection1
    return collection

def add_form(question,qtype,length,answers,anon):
    collection = connect()
    if(collection.find({'question':question}).count() > 0):
        return False
    else:
        d = {'question':question,'qtype':qtype,'length':length,'answers':answers,'anon':anon}
        collection.insert(d)
        return True


def get_question_id(question):
    collection = connect()
    r = [i for i in collection.find({'question':question})]
    if len(r) == 0:
        return
    questionid = r[0]
    return questionid['_id']
