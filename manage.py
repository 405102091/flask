from flask_script import Manager,Server
from app import app
manager=Manager(app)

manager.add_command('dbgserver',Server(host='0.0.0.0',port=5000,use_debugger=True,threaded=True))
manager.add_command('runserver',Server(host='0.0.0.0',port=5000,use_debugger=False,threaded=True))

#python manager.py manager_hello
#@manager.command
#def manager_hello():
#    print('hello')

if __name__ == '__main__':
    manager.run()
