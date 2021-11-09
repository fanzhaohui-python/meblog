# 导入Flask类
from flask import Flask

# 将Flask类的实例 赋值给名为 app的变量，这个实例成为app包的成员
app = Flask(__name__)
print("到低谁在试用我：", __name__)
# 从app包中导入模块routes
from app import routes
