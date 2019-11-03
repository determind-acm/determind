from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from .models import User, Question, TypeInfo, Course, Lesson, UserCourse, db
from app import app
from app.forms import LoginForm, RegistrationForm

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'images/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/user/<username>')
def username(username=""):
    # If student, this:
    #courses = Course.query.filter_by(professor=current_user.id)
    #lessons = {}
    #for course in courses:
    #    lessons[course] = Lesson.query.filter_by(course=course.id)
    usercourses = UserCourse.query.filter_by(user=current_user.id)
    courses = []
    for uc in usercourses:
        courses.append(Course.query.get(uc.course))
    lessons = {}
    for course in courses:
        lessons[course] = Lesson.query.filter_by(course=course.id)
    return render_template('student.html', courses=courses, lessons=lessons)

@app.route('/course/new')
def new_course():
    return render_template('new_course.html')

@app.route('/course/create', methods=["POST"])
def create_course():
    name = request.form['course_name']
    course = Course(name=name, professor=current_user.id)
    db.session.add(course)
    db.session.commit()
    return redirect(url_for('username', username=current_user.username))

@app.route('/course/<id>/lessons/new')
def new_lesson(id=None):
    course = Course.query.get(id)
    size = Lesson.query.filter_by(course=course.id).count()
    lesson = Lesson(course=course.id, index=size+1)
    db.session.add(lesson)
    db.session.commit()
    return redirect(url_for('username', username=current_user.username))

@app.route('/course/<id>/add')
def add_student(id=None):
    course = Course.query.get(id)
    return render_template('add_student.html', course=course)

@app.route('/course/<id>/add', methods=['POST'])
def push_student(id=None):
    name = request.form['student_username']
    user = User.query.filter_by(username=name).first()
    course = Course.query.get(id)
    pair = UserCourse(course=course.id, user=user.id)
    db.session.add(pair)
    db.session.commit()
    return redirect(url_for('username', username=current_user.username))

@app.route('/quiz')
def quiz():
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@app.route('/quiz/results', methods=['POST'])
def results():
    data = []
    for x in range(1, 29):
        data.append(int(request.form['q' + str(x)]))
    dictionary = Question.quizAlgorithm(data)
    return render_template('results.html', dictionary=dictionary)

@app.route('/style/<style>')
def learningstyle(style=None):
    type = TypeInfo.query.get(style)
    return render_template('style.html', style=type)
