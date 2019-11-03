from flask import Flask
import app.models
from app import app
import array as arr

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

linguistic = 0
naturalist = 0
musical = 0
physical = 0
visual = 0
logical = 0
interpersonal = 0
intrapersonal = 0

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

    def quizAlgorithm(arr[]){
        if questionNumber == 1:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                naturalist++;
                break
        if questionNumber == 2:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                musical++;
                break
        if questionNumber == 3:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                physical++;
                break
        if questionNumber == 4:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                visual++
                break
        if questionNumber == 5:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                logical++
                break
        if questionNumber == 6:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                interpersonal++
                break
        if questionNumber == 7:
            if arr[0] == 0:
                linguistic++
                break
            if arr[0] == 1:
                intrapersonal++
                break
        if questionNumber == 8:
            if arr[0] == 0:
                naturalist++
                break
            if arr[0] == 1:
                musical++
                break
        if questionNumber == 9:
            if arr[0] == 0:
                naturalist++
                break
            if arr[0] == 1:
                physical++
                break
        if questionNumber == 10:
            if arr[0] == 0:
                naturalist++
                break
            if arr[0] == 1:
                visual++
                break
        if questionNumber == 11:
            if arr[0] == 0:
                naturalist++
                break
            if arr[0] == 1:
                logical++
                break
        if questionNumber == 12:
            if arr[0] == 0:
                naturalist++
                break
            if arr[0] == 1:
                interpersonal++
                break
        if questionNumber == 13:
            if arr[0] == 0:
                naturalist++
                break
            if arr[0] == 1:
                intrapersonal++
                break
        if questionNumber == 14:
            if arr[0] == 0:
                musical++
                break
            if arr[0] == 1:
                physical++
                break
        if questionNumber == 15:
            if arr[0] == 0:
                musical++
                break
            if arr[0] == 1:
                visual++
                break
        if questionNumber == 16:
            if arr[0] == 0:
                musical++
                break
            if arr[0] == 1:
                logical++
                break
        if questionNumber == 17:
            if arr[0] == 0:
                musical++
                break
            if arr[0] == 1:
                interpersonal++
                break
        if questionNumber == 18:
            if arr[0] == 0:
                musical++
                break
            if arr[0] == 1:
                intrapersonal++
                break
        if questionNumber == 19:
            if arr[0] == 0:
                physical++
                break
            if arr[0] == 1:
                visual++
                break
        if questionNumber == 20:
            if arr[0] == 0:
                physical++
                break
            if arr[0] == 1:
                logical++
                break
        if questionNumber == 21:
            if arr[0] == 0:
                physical++
                break
            if arr[0] == 1:
                interpersonal++
                break
        if questionNumber == 22:
            if arr[0] == 0:
                physical++
                break
            if arr[0] == 1:
                intrapersonal++
                break
        if questionNumber == 23:
            if arr[0] == 0:
                visual++
                break
            if arr[0] == 1:
                logical++
                break
        if questionNumber == 24:
            if arr[0] == 0:
                visual++
                break
            if arr[0] == 1:
                interpersonal++
                break
        if questionNumber == 25:
            if arr[0] == 0:
                visual++
                break
            if arr[0] == 1:
                intrapersonal++
                break
        if questionNumber == 26:
            if arr[0] == 0:
                logical++
                break
            if arr[0] == 1:
                interpersonal++
                break
        if questionNumber == 27:
            if arr[0] == 0:
                logical++
                break
            if arr[0] == 1:
                intrapersonal++
                break
        if questionNumber == 28:
            if arr[0] == 0:
                interpersonal++
                break
            if arr[0] == 1:
                intrapersonal++
                break
                
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
    }
}

    def __repr__(self):
        return '<Question %r>' % self.question
