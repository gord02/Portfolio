# this imports flask as name flask
from flask import Flask
from flask import render_template
from flask import send_file

# this enables flask on the current file i.e __name__ and sets it equal to app
app = Flask(__name__)

# routes are controlled by functions, routes are called decorators and create paths 
@app.route('/')
def index():
# this allows the page index.html to be rendered when route is accessed, html pages MUST be inside TEMPLATE folders
    return render_template("index.html")

@app.route('/resume')
def send_pdf():
    return send_file('static/pdf/resume.pdf', attachment_filename='resume.pdf')

# @app.route('/some')
# def some():
#     return render_template("style.html")

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    return render_template("catchAll.html")
