from flask import Blueprint, request, render_template, g, session, redirect, url_for

from app import db
from app.bulletins.models import Bulletin
from app import requires_login

mod = Blueprint('bulletins', __name__)

@mod.route('/bulletins')
def bulletins_index():
    bulletins = Bulletin.query.order_by(Bulletin.id.desc()).limit(5)
    return render_template('bulletins/index.html', bulletins = bulletins)

@mod.route('/bulletins/<id>')
def bulletins_overview(id):
    bulletin = Bulletin.query.get(id)
    return render_template('bulletins/overview.html', bulletin = bulletin)
