from app import app
from flask import request,render_template,send_from_directory

@app.route('/<path:path>')
def index(path):
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


@app.route('/api/request',methods={'POST','GET'})
def api_request():
    # request.form.get('key',type=str,default=None) # get form data
    # request.args.get('key') # get http-get data
    # request.value.get('key') # get all the pramaters include get and post
    return str(request.values)


@app.route('/api/date',methods={'POST','GET'})
def api_date():
    import time    
    return str(time.ctime())

