#Top-level script that represents the application

#This is where Flask obtains our app instance
from myapp import create_app, db, cli
from myapp.models import User, Post

app = create_app()
cli.register(app)
# When I run flask shell my db & models are there already
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
