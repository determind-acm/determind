from flask import render_template
from app import app

@app.route('/')

@app.route('/home')
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

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user/<username>')
def username(username=""):
    return ('username.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/quiz/results')
def results():
    return render_template('results.html')

@app.route('learningstyles/<styles>')
def learningstyle(styles=""):
    return render_template('learningstyle')
