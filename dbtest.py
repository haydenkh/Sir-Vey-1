import db

db.drop_collection2()
db.drop_collection1()

db.add_form("How do you do?","Text", ['good'] , False )
db.add_form("How do you do?","mc",['hood'], False)
db.add_form("How is the weather?","mc",['good','great'], True)


id = db.get_question_id("How do you do?")
q = db.get_question(id)



#db.send_question("This should not exsist",["allo","Eliftw@gmail.com"])
db.send_question("How is the weather?",["Eliftw@gmail.com","Patrick"])
#db.send_question("What?",['Eliftw@gmail.com'])
#x = db.get_results()
#print db.get_recipient(x[0])
print db.get_recipient_questions("Eliftw@gmail.com")
print db.get_recipient_questions("Patrick")
#print "answer id"
#print x
#print x[0]
#print "ready"
#db.set_answer(x[0],'3')
#print db.get_answer(x[0])
#print db.get_recipient_questions("Eliftw@gmail.com")



forms=db.get_forms()
qtype=db.get_qtype("How do you do?")
answer=db.get_answers("How do you do?")
anon=db.get_anon("How do you do?")





#print forms
#print "How do you do?"
#print qtype
#print answer
#print anon


