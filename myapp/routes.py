# Define the logic of the application
from inspect import EndOfBlock
from flask import render_template, flash, redirect, url_for
from flask.helpers import get_flashed_messages
from flask_login import login_user, current_user
from flask_migrate import current
from myapp import app
from myapp.forms import LoginForm
from myapp.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'natalia'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #form is submitted & valid
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
