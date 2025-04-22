from flask import render_template, Blueprint, send_file
methodology = Blueprint('methodology', __name__)

@methodology.route('/methodology')
def page():
  return render_template('methodology.html')

@methodology.route('/downloadPaper')
def download ():
    path = "./static/downloadable/Carbon-App-Paper-Group-3-2025.pdf"
    return send_file(path, as_attachment=True)