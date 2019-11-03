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

linguistic = 0
naturalist = 0
musical = 0
physical = 0
visual = 0
logical = 0
interpersonal = 0
intrapersonal = 0

class Question(db.Model):

    question = db.Column(db.String(100), nullable=False)
    answer1 = db.Column(db.String(100), nullable=False)
    answer2 = db.Column(db.String(100), nullable=False)
    questionNumber = db.Column(db.Integer, primary_key=True)

    def quizAlgorithm(arr):
        if questionNumber == 1:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                naturalist += 1;

        if questionNumber == 2:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                musical += 1;

        if questionNumber == 3:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                physical += 1;

        if questionNumber == 4:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                visual += 1

        if questionNumber == 5:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                logical += 1

        if questionNumber == 6:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                interpersonal += 1

        if questionNumber == 7:
            if arr[0] == 0:
                linguistic += 1

            if arr[0] == 1:
                intrapersonal += 1

        if questionNumber == 8:
            if arr[0] == 0:
                naturalist += 1

            if arr[0] == 1:
                musical += 1

        if questionNumber == 9:
            if arr[0] == 0:
                naturalist += 1

            if arr[0] == 1:
                physical += 1

        if questionNumber == 10:
            if arr[0] == 0:
                naturalist += 1

            if arr[0] == 1:
                visual += 1

        if questionNumber == 11:
            if arr[0] == 0:
                naturalist += 1

            if arr[0] == 1:
                logical += 1

        if questionNumber == 12:
            if arr[0] == 0:
                naturalist += 1

            if arr[0] == 1:
                interpersonal += 1

        if questionNumber == 13:
            if arr[0] == 0:
                naturalist += 1

            if arr[0] == 1:
                intrapersonal += 1

        if questionNumber == 14:
            if arr[0] == 0:
                musical += 1

            if arr[0] == 1:
                physical += 1

        if questionNumber == 15:
            if arr[0] == 0:
                musical += 1

            if arr[0] == 1:
                visual += 1

        if questionNumber == 16:
            if arr[0] == 0:
                musical += 1

            if arr[0] == 1:
                logical += 1

        if questionNumber == 17:
            if arr[0] == 0:
                musical += 1

            if arr[0] == 1:
                interpersonal += 1

        if questionNumber == 18:
            if arr[0] == 0:
                musical += 1

            if arr[0] == 1:
                intrapersonal += 1

        if questionNumber == 19:
            if arr[0] == 0:
                physical += 1

            if arr[0] == 1:
                visual += 1

        if questionNumber == 20:
            if arr[0] == 0:
                physical += 1

            if arr[0] == 1:
                logical += 1

        if questionNumber == 21:
            if arr[0] == 0:
                physical += 1

            if arr[0] == 1:
                interpersonal += 1

        if questionNumber == 22:
            if arr[0] == 0:
                physical += 1

            if arr[0] == 1:
                intrapersonal += 1

        if questionNumber == 23:
            if arr[0] == 0:
                visual += 1

            if arr[0] == 1:
                logical += 1

        if questionNumber == 24:
            if arr[0] == 0:
                visual += 1

            if arr[0] == 1:
                interpersonal += 1

        if questionNumber == 25:
            if arr[0] == 0:
                visual += 1

            if arr[0] == 1:
                intrapersonal += 1

        if questionNumber == 26:
            if arr[0] == 0:
                logical += 1

            if arr[0] == 1:
                interpersonal += 1

        if questionNumber == 27:
            if arr[0] == 0:
                logical += 1

            if arr[0] == 1:
                intrapersonal += 1

        if questionNumber == 28:
            if arr[0] == 0:
                interpersonal += 1

            if arr[0] == 1:
                intrapersonal += 1


        dictionary = {
            "Linguistic: ":linguistics,
            "Naturalist: ":naturalist,
            "Musical: ":musical,
            "Physical: ":physical,
            "Visual: ":visual,
            "Logical: ":logical,
            "Interpersonal: ":interpersonal,
            "Intrapersonal: ":intrapersonal
        }

        return dictionary

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
