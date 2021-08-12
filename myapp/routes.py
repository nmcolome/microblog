# Define the logic of the application
from inspect import EndOfBlock
from flask import render_template, flash, redirect
from flask.helpers import get_flashed_messages
from myapp import app
from myapp.forms import LoginForm

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
    form = LoginForm()
    if form.validate_on_submit():
        #form is submitted & valid
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
