from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app=Flask(__name__)
app.config.from_object('config') # 从config.py读取配置文件
limiter=Limiter(
    app,
    key_func=get_remote_address,
#    default_limits=['200 per day','60 per minute']
    default_limits=['3600 per minute',]
)

from app import views,models,apis

