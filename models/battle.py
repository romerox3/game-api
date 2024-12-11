from . import db

class Battle(db.Model):
    __tablename__ = 'battle'
    id = db.Column(db.Integer, primary_key=True)
    character1_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    character2_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    rounds = db.Column(db.Integer, default=0)
    result = db.Column(db.String, nullable=True)
    environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'), nullable=False)

    character1 = db.relationship('Character', foreign_keys=[character1_id])
    character2 = db.relationship('Character', foreign_keys=[character2_id])
    environment = db.relationship('Environment')