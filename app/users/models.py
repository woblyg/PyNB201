from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(36))
    email = db.Column(db.String(36))
    password = db.Column(db.String(54))
    role = db.Column(db.Integer(1))
    regtime = db.Column(db.DateTime)
    
    def __init__(self, name = None, email = None, password = None, role = None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.regtime = datetime.now()
    
    def __repr__(self):
        return('<User %r>' % (self.id))
