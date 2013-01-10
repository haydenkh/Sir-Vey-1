import db

db.drop_collection2()


db.add_form("How do you do?","Text", ['good'] , False )
db.add_form("How do you do?","mc",['hood'], False)
db.add_form("How is the weather?","mc",['good','great'], True)


id = db.get_question_id("How do you do?")
q = db.get_question(id)



db.send_question("Hey!",["Eliftw@gmail.com","PatrickStar@gmail.com"])
db.send_question("Hey Patrick!",["PatrickStar@gmail.com"])



#x = db.get_results()
#print db.get_recipient(x[0])
x = db.get_recipient_answerids("PatrickStar@gmail.com")
print x[0]

forms=db.get_forms()
qtype=db.get_qtype("How do you do?")
answer=db.get_answers("How do you do?")
anon=db.get_anon("How do you do?")





#print forms
#print "How do you do?"
#print qtype
#print answer
#print anon


