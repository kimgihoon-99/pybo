# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:42:40 2025

@author: Admin
"""
from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))

'''
'main'
=> Blueprint의 별칭 

__name__
=> main_views

url_prefix='/'
=> localhost:5000/

ex) url_prefix='/main'
=> localhost:5000/main/
'''



'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return 'User %s' % name

@app.route('/hi/<user>')
def hi(user):
    return render_template('hello.html', name=user)

if __name__ == '__main__':
    app.run(debug=True)

'''

'''

@app.route("/")
def index():
    return "Flask App!"

@app.route("/user/")
def hello():
    users = ["Frank", "Steve", "Alice", "Bruce"]
    var = 1
    return render_template('user.html', **locals())
'''



'''
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest'% guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect('/admin')
    else:
        return redirect(url_for("hello_guest", guest = name))



if __name__ == '__main__':
    app.run(debug=True)

'''


'''
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('asd.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s'% name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))


if __name__ == '__main__':
    app.run(debug=True)


'''











































