from flask import render_template, Blueprint
about = Blueprint('about', __name__)

@about.route('/about')
def page():
  return render_template('about.html')