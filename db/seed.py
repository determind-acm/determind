from determind import Question

class Seed:
    def main():
        f=open("Questions.txt", "r")
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

