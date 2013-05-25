from flask import Blueprint, request, render_template, g, session, redirect, url_for

from app import db
from app.personnel.models import Personnel
from app import requires_login

mod = Blueprint('personnel', __name__)
