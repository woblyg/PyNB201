from app import db

TYPE = [
    'fire',
    'storm',
    'flood'
]

SEVERITY = [
    'low',
    'high',
    'extreme',
    'cataclysmic'
]

class Disaster(db.Model):
    __tablename__ = 'disasters'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    type = db.Column(db.Integer)
    location = db.Column(db.Integer(4)) ## Postcode.
    severity = db.Column(db.Integer(1))
    public = db.Column(db.Integer(1))
    reporttime = db.Column(db.DateTime)
    
    def __init__(self, name = None, type = None, location = None, severity = None, public = None):
        self.name = Name
        self.type = type
        self.location = location
        self.severity = severity
        self.public = public
    
    def __repr__(self):
        return('<Disaster %r>' % (self.id))
    
    def getType(self):
        return TYPE[self.type]

    def getSeverity(self):
        return SEVERITY[self.severity]
