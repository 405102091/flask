from app import app
from flask import render_template,send_from_directory

@app.route('/')
def index():
    return 'hello world!'

@app.route('/file/<path:path>')
def send_file(path):
    return send_from_directory('./file',path)
