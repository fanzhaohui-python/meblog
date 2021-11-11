from flask import render_template

from app import app


# 2个路由
@app.route('/')
@app.route("/index")
@app.route("/index/")
# 1个视图函数
def index():
    user = {"username": "zhouyj"}
    posts = [
        {'author': {'username': 'fanzh'}, 'body': 'Beautiful day in　Portland!'},
        {'author': {'username': 'zhouyj'}, 'body': 'this is aaalll girl!'}
    ]
    return render_template('index.html', title=None, user=user, posts=posts)  # 返回一个字符串
