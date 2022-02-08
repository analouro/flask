from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymsql://root:root@localhost:3306/flask_practice'

db2 = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)