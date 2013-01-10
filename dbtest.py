import db

db.add_form("How do you do?","Text", ['good'] , False )
db.add_form("How do you do?","mc",['hood'], False)
db.add_form("How is the weather?","mc",['good','great'], True)

id = db.get_question_id("How do you do?")
q = db.get_question(id)
print "IDTEST"
print q


db.send_question("How do you do?","Eliftw@gmail.com")

mail = db.get_results()
for i in mail:
    print db.get_answer((i))
    print db.get_question_r(i)

forms=db.get_forms()
qtype=db.get_qtype("How do you do?")
answer=db.get_answers("How do you do?")
anon=db.get_anon("How do you do?")





print forms
print "How do you do?"
print qtype
print answer
print anon


