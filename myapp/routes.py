# Define the logic of the application
from myapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'natalia'}
    return render_template('index.html', title='Home', user=user)
