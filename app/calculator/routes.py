from flask import render_template, Blueprint
calculator = Blueprint('calculator', __name__)

@calculator.route('/calculator')
def page():
  return render_template('calculator.html')