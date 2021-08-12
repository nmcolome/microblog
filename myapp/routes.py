# Define the logic of the application
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'