from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.models import User
from app.disasters.models import Disaster
from app.bulletins.models import Bulletin

mod = Blueprint('admin', __name__)

@mod.before_request
def admin_before_request():
    if not g.user or g.user.role < 3:
        return redirect(url_for('not_found'))

@mod.route('/admin')
def admin():
    return render_template('admin/index.html')

@mod.route('/admin/users')
def admin_users():
    users = User.query.order_by(User.id.asc())
    return render_template('admin/users/index.html', users = users)

@mod.route('/admin/users/add', methods = ['GET', 'POST'])
def admin_users_add():
    if request.method == 'GET':
        return render_template('/admin/users/add.html')
    else:
        user = User(request.form['user-name'], request.form['user-email'], generate_password_hash(request.form['user-password']), request.form['user-role'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin.admin_users') + '#add')

@mod.route('/admin/users/edit/<id>', methods = ['GET', 'POST'])
def admin_users_edit(id):
    user = User.query.get(id)
    if request.method == 'GET':
        return render_template('/admin/users/edit.html', user = user)
    else:
        user.name = request.form['user-name']
        user.email = request.form['user-email']
        if request.form['user-password'] != '':
            user.password = generate_password_hash(request.form['user-password'])
        user.role = request.form['user-role']
        db.session.commit()
        return redirect(url_for('admin.admin_users') + '#edit')

@mod.route('/admin/disasters')
def admin_disasters():
    disasters = Disaster.query.order_by(Disaster.id.asc())
    return render_template('admin/disasters/index.html', disasters = disasters)

@mod.route('/admin/disasters/add', methods = ['GET', 'POST'])
def admin_disasters_add():
    if request.method == 'GET':
        return render_template('/admin/disasters/add.html')
    else:
        disaster = Disaster(request.form['disaster-name'], request.form['disaster-location'], request.form['disaster-severity'], request.form['disaster-type'])
        db.session.add(disaster)
        db.session.commit()
        return redirect(url_for('admin.admin_disasters') + '#add')
    
@mod.route('/admin/disasters/edit/<id>')
def admin_disasters_edit(id):
    disaster = Disaster.query.get(id)
    if request.method == 'GET':
        return render_template('/admin/disasters/edit.html', disaster = disaster)
    else:
        disaster.name = request.form['disaster-name']
        disaster.location = request.form['disaster-location']
        disaster.severity = request.form['disaster-severity']
        disaster.type = request.form['disaster-type']
        db.session.commit()
        return redirect(url_for('admin.admin_disasters') + '#edit')

@mod.route('/admin/personnel')
def admin_personnel(id):
    return render_template('admin/personnel/index.html')

@mod.route('/admin/personnel/add', methods = ['GET', 'POST'])
def admin_personnel_add():
    if request.method == 'GET':
        return render_template('/admin/personnel/add.html')
    else:
        personnel = Personnel(request.form['personnel-name'], request.form['personnel-email'], request.form['personnel-location'], request.form['personnel-role'])
        db.session.add(personnel)
        db.session.commit()
        return redirect(url_for('admin.admin_personnel') + '#add')

@mod.route('/admin/personnel/edit/<id>', methods = ['GET', 'POST'])
def admin_personnel_edit(id):
    personnel = Personnel.query.get(id)
    if request.method == 'GET':
        return render_template('/admin/personnel/edit.html', personnel = personnel)
    else:
        personnel.name = request.form['personnel-name']
        personnel.email = request.form['personnel-email']
        personnel.location = request.form['location']
        if personnel.location == 0:
            personnel.deployed = 0
        else:
            personnel.deployed = 1
        personnel.role = request.form['role']
        db.session.commit()
        return redirect(url_for('admin.admin_personnel') + '#edit')
