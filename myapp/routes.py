# Define the logic of the application
from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
