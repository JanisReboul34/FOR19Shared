from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
application.config['SECRET_KEY'] = '9240d4b7a0f0f659e11c060f4825a51ecc3323cf2e99fdc4'

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
application.config['SQLALCHEMY_BINDS'] ={'transport': 'sqlite:///transport.db'}
db = SQLAlchemy(application)

from app.about.routes import about
from app.home.routes import home
from app.methodology.routes import methodology
from app.calculator.routes import calculator
from app.profile.routes import profile
from app.users.routes import users

application.register_blueprint(about)
application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(calculator)
application.register_blueprint(profile)
application.register_blueprint(users)

