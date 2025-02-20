from flask import Flask

application = Flask(__name__)

from app.about.routes import about
from app.home.routes import home
from app.methodology.routes import methodology
from app.calculator.routes import calculator

application.register_blueprint(about)
application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(calculator)