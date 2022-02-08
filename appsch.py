from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymsql://root:root@localhost:3306/flask_practice'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///datasch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Shopping(db.Model):
    shopping_id = db.Column(db.Integer, primary_key=True)
    # id_user_fk = id
    purchase = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    payment = db.Column(db.Boolean, default=True) # default = True - allows us to set a default automatically, otherwise we would have to add on createsch.py if payment was true or false.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
