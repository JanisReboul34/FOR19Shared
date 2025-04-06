from flask import render_template, Blueprint, redirect, flash, url_for
from app.users.forms import RegistrationForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      return redirect(url_for('home.page'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  return render_template('users/login.html', title='login')


