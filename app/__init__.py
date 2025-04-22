from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view='users.login'
login_manager.login_message_category='info'

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

