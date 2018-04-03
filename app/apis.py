from app import app
from flask import request,render_template,send_from_directory,jsonify,make_response

@app.route('/api/request',methods={'POST','GET'})
def api_request():
    # request.form.get('key',type=str,default=None) # get form data
    # request.args.get('key') # get http-get data
    # request.value.get('key') # get all the pramaters include get and post
    return str(request.values)


@app.route('/api/date',methods={'POST','GET'})
def api_date():
    import time
    return allow_ajax(jsonify(serverdate=str(time.ctime())))

@app.route('/api/randint',methods={'POST','GET'})
def api_randint():
    import random    
    print(request.values)
    randmax=request.values.get('MAX',100,type=int)
    randmin=request.values.get('MIN',0,type=int)
    randlen=request.values.get('LEN',1,type=int)
    return allow_ajax(jsonify(randint=[random.randint(randmin,randmax) for i in range(randlen)]))
    
def allow_ajax(res):
    response=make_response(res)
    response.headers['Access-Control-Allow-Origin'] = '*'  
    response.headers['Access-Control-Allow-Methods'] = 'POST'  
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
    return response 
