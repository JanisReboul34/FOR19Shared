from flask import render_template, Blueprint, send_file
methodology = Blueprint('methodology', __name__)

@methodology.route('/methodology')
def page():
  return render_template('methodology.html')

@methodology.route('/downloadPaper')
def download ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./static/downloadable/Essay Green App.pdf"
    return send_file(path, as_attachment=True)