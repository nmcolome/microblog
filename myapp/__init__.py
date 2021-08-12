#Defines what the package exposes to the outside world
from flask import Flask

app = Flask(__name__)

from myapp import routes
