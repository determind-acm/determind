from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/user/<username>', )
def username(username=""):
    # If student, this:
    return render_template('student.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/quiz/results')
def results():
    return render_template('results.html')

@app.route('/style/<styles>')
def learningstyle(styles=""):
    return render_template('style.html')
