from flask import render_template, Blueprint, redirect, flash, url_for
from app.users.forms import RegistrationForm, LoginForm
from app.models import User
from app import db, bcrypt

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! Now you are able to Login!','succsess')
      return redirect(url_for('home.page'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'fjell@demo.com' and form.password.data == 'regn':
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect(url_for('home.page'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('users/login.html', title='login', form=form)


