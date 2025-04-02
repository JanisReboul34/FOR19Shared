from flask import render_template, Blueprint
about = Blueprint('profile', __name__)

@about.route('/profile')
def page():
  return render_template('about.html')