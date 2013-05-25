from flask import Blueprint, request, render_template, g, session, redirect, url_for

from app import db
from app.bulletins.models import Bulletin
from app import requires_login

mod = Blueprint('bulletins', __name__)
