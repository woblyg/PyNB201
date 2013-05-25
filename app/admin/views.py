from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.models import User
from app import requires_login

mod = Blueprint('users', __name__)

@mod.before_request
def admin_before_request():
    if not g.user or g.user.role < 3:
        return redirect(url_for('not_found'))

@mod.route('/admin')
def login():
    return render_template('admin/index.html')

"""
    ### Users
    General users of the system - Officials, Premier, Sysadmin
"""

@mod.route('/admin/users')
def admin_users():
    return render_template('admin/users/index.html')

@mod.route('/admin/users/add', method = ['GET', 'POST'])
def admin_users_add():
    if request.method == 'GET':
        return render_template('/admin/users/add.html')
    else:
        user = User(request.form['user-name'], request.form['user-email'], generate_password_hash(request.form['user-password']), request.form['user-role'])
        db.session.add(user)
        db.session.commit()
        return render_template(url_for('admin.admin_users') + '#add')

@mod.route('/admin/users/edit/<id>')
def admin_users_edit(id):
    user = User.query.get(id)
    if request.method == 'GET':
        return render_template('/admin/users/edit.html', user = user)
    else:
        user.name = request.form['user-name']
        user.email = request.form['user-email']
        db.session.commit()
        return render_template(url_for('admin.admin_users') + '#edit')

"""
    ### Disasters ###
    Zones with a disaster hit. Personnel are deployed to here.
"""

@mod.route('/admin/disasters')
def admin_disasters():
    return render_template('admin/disasters/index.html')

@mod.route('/admin/disasters/add', method = ['GET', 'POST'])
def admin_disasters_add():
    if request.method == 'GET':
        return render_template('/admin/disasters/add.html')
    else:
        disaster = Disaster(request.form['disaster-name'], request.form['disaster-location'], request.form['disaster-severity'], request.form['disaster-type'])
        db.session.add(disaster)
        db.session.commit()
        return render_template(url_for('admin.admin_disasters') + '#add')
    
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
        return render_template(url_for('admin.admin_disasters') + '#edit')

"""
    ### Personnel ###
    Deployed persons to an emergency area.
"""

@mod.route('/admin/personnel')
def admin_personnel(id):
    return render_template('admin/personnel/index.html')

@mod.route('/admin/personnel/add', method = ['GET', 'POST'])
def admin_personnel_add():
    if request.method == 'GET':
        return render_template('/admin/personnel/add.html')
    else:
        personnel = Personnel(request.form['personnel-name'], request.form['personnel-email'], request.form['personnel-location'], request.form['personnel-role'])
        db.session.add(personnel)
        db.session.commit()
        return render_template(url_for('admin.admin_personnel') + '#add')

@mod.route('/admin/personnel/edit/<id>', method = ['GET', 'POST'])
def admin_personnel_edit(id):
    personnel = Personnel.query.get(id)
    if request.method == 'GET':
        return render_template('/admin/personnel/edit.html'. personnel = personnel)
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
        return render_template(url_for('admin.admin_personnel') + '#edit')
