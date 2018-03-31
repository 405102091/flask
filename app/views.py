from app import app
from flask import request,render_template,send_from_directory,url_for,redirect

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<path:path>')
def other_page(path):
    if path=='favicon.ico':
        return redirect(url_for('send_icons',path='favicon.ico'))
    return render_template(path) # auto search in templates folder

@app.route('/file/<path:path>')
def send_file(path):
    return send_from_directory('./file',path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js',path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css',path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('./static/images',path)

@app.route('/icons/<path:path>')
def send_icons(path):
    return send_from_directory('./static/icons',path)



