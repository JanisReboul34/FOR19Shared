from flask import Flask, render_template, send_file
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

@application.route('/methodology')
def methodology():
  return render_template('methodology.html')

@application.route('/downloadFile')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./static/downloadable/Transport Carbon App.pdf"
    return send_file(path, as_attachment=True)


if __name__=='__main__':
  application.run(debug=True)  