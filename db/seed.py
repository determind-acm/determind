from determind import Question
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

class Seed:
    def main():
        f=open("questions.txt", "r")
        f1=f.readlines()
        for num, line in enumerate(f1, start=1):
            if (num % 3 == 0):
                answer2 = line
                dbline = Question(question, answer1, answer2)
                db.session.add(dbline)
                db.session.commit()
            elif (num % 2 == 0):
                answer1 = line
                dbline = Question(question, answer1, answer2)
                db.session.add(dbline)
                db.session.commit()
            else:
                question = line
                dbline = Question(question, answer1, answer2)
                db.session.add(dbline)
                db.session.commit()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

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
