from flask import render_template, Blueprint
from app.models import Transport #Need this line for the databases to work:) (I think?)

calculator = Blueprint('calculator', __name__)

@calculator.route('/calculator')
def page():
  return render_template('calculator.html')