from flask import Blueprint, request, render_template, g, session, redirect, url_for

from app import db
from app.disasters.models import Disaster
from app import requires_login

mod = Blueprint('disasters', __name__)

@mod.route('/disasters')
def disasters_index():
    disasters = Disaster.query.order_by(Disaster.id.desc()).limit(25)
    return render_template('disasters/index.html', disasters = disasters)

@mod.route('/disasters/<id>')
def disaster_overview(id):
    disaster = Disaster.query.get(id)
    return render_template('disasters/overview.html', disaster = disaster)
