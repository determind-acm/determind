from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Boolean)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Question(db.Model):

    question = db.Column(db.String(100), nullable=False)
    answer1 = db.Column(db.String(100), nullable=False)
    answer2 = db.Column(db.String(100), nullable=False)
    questionNumber = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Question %r>' % self.question

class TypeInfo(db.Model):

    key = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    alternates = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    traits = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Type %r>' % self.type
