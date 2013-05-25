from flask import Blueprint, request, render_template, g, session, redirect, url_for

from app import db
from app.disasters.models import Disaster
from app import requires_login

mod = Blueprint('disasters', __name__)
