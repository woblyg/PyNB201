from app import db
 
ROLE = [
    'fire',
    'police',
    'ambulance'
]
 
class Personnel(db.Model):
    __tablename__ = 'personnel'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(36))
    role = db.Column(db.Integer(1))
    deployed = db.Column(db.Integer(1))
    location = db.Column(db.Integer(4))
    
    def __init__(self, name = None, email = None, password = None):
        self.name = name
        self.email = email
        self.password = password
    
    def getRole(self):
        return ROLE[self.role]
    
    def __repr__(self):
        return('<User %r>' % (self.id))
