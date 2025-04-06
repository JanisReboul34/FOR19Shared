from flask import render_template, Blueprint
from app.models import User, Transport

home=Blueprint('home',__name__)

@home.route('/')
def page():
  return render_template('home.html')