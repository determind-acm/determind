from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Question(db.Model):

    question = db.Column(db.String(100), unique=True, nullable=False)
    answer1 = db.Column(db.String(100), unique=True, nullable=False)
    answer2 = db.Column(db.String(100), unique=True, nullable=False)
    questionNumber = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
        
    def __repr__(self):
        return '<Question %r>' % self.question
