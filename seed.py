from app.models import Question, TypeInfo
from app.models import db
import math

class Seed:
    def main():
        f = open("questions.txt", "r")
        lines = f.readlines();
        for i in range(math.ceil(len(lines) / 4)):
            dbline = Question(question=lines[4*i], answer1=lines[4*i+1], answer2=lines[4*i+2])
            db.session.add(dbline)
        db.session.commit()

        f = open("research.txt", "r")
        lines = f.readlines();
        for i in range(math.ceil(len(lines) / 6)):
            dbline = TypeInfo(key=lines[6*i].strip(), name=lines[6*i+1].strip(), alternates=lines[6*i+2].strip(), description=lines[6*i+3].strip(), traits=lines[6*i+4].strip())
            db.session.add(dbline)
        db.session.commit()

Seed.main()
