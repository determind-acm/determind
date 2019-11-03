from app.models import *
import math

class Seed:
    def main():
        f = open("questions.txt", "r")
        lines = f.readlines();
        for i in range(math.ceil(len(lines) / 4)):
            print(lines[4*i])
            dbline = Question(question=lines[4*i], answer1=lines[4*i+1], answer2=lines[4*i+2])
            db.session.add(dbline)
        db.session.commit()

Seed.main()
