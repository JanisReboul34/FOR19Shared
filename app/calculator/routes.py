from flask import render_template, Blueprint
from app.models import Transport #Need this line for the databases to work:) (I think?)
#Han gjør noe mer her 10c 6.43, men tror ikke det er nødvendig for login/logout

calculator = Blueprint('calculator', __name__)

@calculator.route('/calculator')
def page():
  return render_template('calculator.html')