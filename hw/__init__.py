import flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

# instance of the Flask class
hw_obj = flask.Flask(__name__)
hw_obj.config.from_mapping(
        SECRET_KEY = 'it-dont-matter',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False

)

db = SQLAlchemy(hw_obj)

login = LoginManager(hw_obj)
login.login_view = 'login'

from hw import models, forms
