from flask import render_template, Blueprint
profile = Blueprint('profile', __name__)

@profile.route('/profile')
def page():
  return render_template('profile.html')