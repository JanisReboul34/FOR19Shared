from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def home():
  return render_template('home.html')

@application.route('/calculator')
def calculator():
  return render_template('calculator.html')

@application.route('/about')
def about():
  return render_template('about.html')



if __name__=='__main__':
  application.run(debug=True)  