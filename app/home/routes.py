from flask import render_template, Blueprint
home = Blueprint('home', __name__)

@home.route('/')
def page():
  return render_template('home.html')