from functools import wraps
from flask import Flask, g, redirect, render_template, request, session
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xcaV$\xb7\xb3\xa0%\xa6\xe9U\x02\x85\x7f\x9f0\x8a\xbf\xea\xa7\x1a\xbbiR'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///pynb201?unix_socket=/run/mysqld/mysqld.sock'
db = SQLAlchemy(app)

from app.users.models import User

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('users.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function

@app.before_request
def before_request():
    g.user = None
    if 'uid' in session:
        g.user = User.query.get(session['uid'])

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

from app.admin.views import mod as adminMod
from app.bulletins.views import mod as bulletinsMod
from app.disasters.views import mod as disastersMod
from app.personnel.views import mod as personnelMod
from app.users.views import mod as usersMod

app.register_blueprint(adminMod)
app.register_blueprint(bulletinsMod)
app.register_blueprint(disastersMod)
app.register_blueprint(personnelMod)
app.register_blueprint(usersMod)
