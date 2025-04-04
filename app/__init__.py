from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

from app.about.routes import about
from app.home.routes import home
from app.methodology.routes import methodology
from app.calculator.routes import calculator
from app.profile.routes import profile

application.register_blueprint(about)
application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(calculator)
application.register_blueprint(profile)

