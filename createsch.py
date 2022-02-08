from appsch import db, Users, Shopping

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty', last_name='Toot')
testshop = Shopping(purchase='Tshirt', value=10.2)
db.session.add(testuser)
db.session.add(testshop)
db.session.commit()
