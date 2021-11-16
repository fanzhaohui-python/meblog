# 导入Flask类
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 将Flask类的实例 赋值给名为 app的变量，这个实例成为app包的成员
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# print("到低谁在试用我：", __name__)
# 从app包中导入模块routes
from app import routes,models
