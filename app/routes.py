from flask import render_template
from flask_login import current_user, login_user, logout_user
from app.seed import User
from app import app

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
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(users, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

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
