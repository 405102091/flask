from flask import Flask
app=Flask(__name__)
app.config.from_object('config') # 从config.py读取配置文件
from app import views,models,apis

