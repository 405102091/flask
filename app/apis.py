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
    return str(time.ctime())

@app.route('/api/randint',methods={'POST','GET'})
def api_randint():
    import random    
    parmax=request.values.get('MAX')
    randmax=100 if parmax==None else int(parmax)
    parmin=request.values.get('MIN')
    randmin=0 if parmin==None else int(parmin)
    parlen=request.values.get('LEN')
    randlen=1 if parlen==None else int(parlen)
    if randlen==1:
        return allow_ajax(jsonify(randint=random.randint(randmin,randmax)))
    elif randlen>1:
        return allow_ajax(jsonify(randint=[random.randint(randmin,randmax) for i in range(randlen)]))
    
def allow_ajax(res):
    response=make_response(res)
    response.headers['Access-Control-Allow-Origin'] = '*' 
    return response 
    #response.headers['Access-Control-Allow-Methods'] = 'POST'  
    #response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
