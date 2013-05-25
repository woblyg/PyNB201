from app import db

class Bulletin(db.Model):
    __tablename__ = 'bulletins'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(36))
    body = db.Column(db.String)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    disaster = db.Column(db.Integer, db.ForeignKey('disasters.id'))
    posttime = db.Column(db.DateTime)
    
    bulletinauthor = db.relationship('User', lazy = 'joined')
    bulletindisaster = db.relationship('Disaster', lazy = 'joined')
