from app import app
from flask import request,render_template,send_from_directory

@app.route('/')
def index():
    return 'hello world!'

@app.route('/file/<path:path>')
def send_file(path):
    return send_from_directory('./file',path)

@app.route('/api/request',methods={'POST','GET'})
def api_get():
    # request.form.get('key',type=str,default=None) # get form data
    # request.args.get('key') # get http-get data
    # request.value.get('key') # get all the pramaters include get and post
    return str(request.values)
