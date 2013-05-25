from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.models import User
from app import requires_login

mod = Blueprint('users', __name__)

@mod.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    else:
        user = User.query.filter_by(email = request.form['login-email']).first()
        if user and check_password_hash(user.password, request.form['login-password']):
            session['uid'] = user.id
            return redirect(url_for('index'))
        else:
            return render_template('user/login.html' + '#badlogin')   
