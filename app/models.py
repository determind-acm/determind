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

    @staticmethod
    def quizAlgorithm(arr):

        linguistic = 0
        naturalist = 0
        musical = 0
        physical = 0
        visual = 0
        logical = 0
        interpersonal = 0
        intrapersonal = 0

        if arr[0] == 0:
            linguistic += 1

        if arr[0] == 1:
            naturalist += 1;

        if arr[1] == 0:
            linguistic += 1

        if arr[1] == 1:
            musical += 1;

        if arr[2] == 0:
            linguistic += 1

        if arr[2] == 1:
            physical += 1;

        if arr[3] == 0:
            linguistic += 1

        if arr[3] == 1:
            visual += 1

        if arr[4] == 0:
            linguistic += 1

        if arr[4] == 1:
            logical += 1

        if arr[5] == 0:
            linguistic += 1

        if arr[5] == 1:
            interpersonal += 1

        if arr[6] == 0:
            linguistic += 1

        if arr[6] == 1:
            intrapersonal += 1

        if arr[7] == 0:
            naturalist += 1

        if arr[7] == 1:
            musical += 1

        if arr[8] == 0:
            naturalist += 1

        if arr[8] == 1:
            physical += 1

        if arr[9] == 0:
            naturalist += 1

        if arr[9] == 1:
            visual += 1

        if arr[10] == 0:
            naturalist += 1

        if arr[10] == 1:
            logical += 1

        if arr[11] == 0:
            naturalist += 1

        if arr[11] == 1:
            interpersonal += 1

        if arr[12] == 0:
            naturalist += 1

        if arr[12] == 1:
            intrapersonal += 1

        if arr[13] == 0:
            musical += 1

        if arr[13] == 1:
            physical += 1

        if arr[14] == 0:
            musical += 1

        if arr[14] == 1:
            visual += 1

        if arr[15] == 0:
            musical += 1

        if arr[15] == 1:
            logical += 1

        if arr[16] == 0:
            musical += 1

        if arr[16] == 1:
            interpersonal += 1

        if arr[17] == 0:
            musical += 1

        if arr[17] == 1:
            intrapersonal += 1

        if arr[18] == 0:
            physical += 1

        if arr[18] == 1:
            visual += 1

        if arr[19] == 0:
            physical += 1

        if arr[19] == 1:
            logical += 1

        if arr[20] == 0:
            physical += 1

        if arr[20] == 1:
            interpersonal += 1

        if arr[21] == 0:
            physical += 1

        if arr[21] == 1:
            intrapersonal += 1

        if arr[22] == 0:
            visual += 1

        if arr[22] == 1:
            logical += 1

        if arr[23] == 0:
            visual += 1

        if arr[23] == 1:
            interpersonal += 1

        if arr[24] == 0:
            visual += 1

        if arr[24] == 1:
            intrapersonal += 1

        if arr[25] == 0:
            logical += 1

        if arr[25] == 1:
            interpersonal += 1

        if arr[26] == 0:
            logical += 1

        if arr[26] == 1:
            intrapersonal += 1

        if arr[27] == 0:
            interpersonal += 1

        if arr[27] == 1:
            intrapersonal += 1


        dictionary = {
            "linguistic": linguistic,
            "naturalist":naturalist,
            "musical":musical,
            "physical":physical,
            "visual":visual,
            "logical":logical,
            "interpersonal":interpersonal,
            "intrapersonal":intrapersonal
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

class Course(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    professor = db.Column(db.Integer, nullable=False, foreign_key(User.id))

    def __repr__(self):
        return '<Course %r>' % self.course

class Lesson(db.Model):

    index = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Integer, nullable=False, foreign_key(User.id))

    def __repr__(self):
        return '<Lesson %r>' % self.lesson
