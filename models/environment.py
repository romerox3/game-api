from . import db

class Environment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    effect_type = db.Column(db.String(100), nullable=True)
    attack_modifier = db.Column(db.Float, default=1.0)
    defense_modifier = db.Column(db.Float, default=1.0)
    dodge_modifier = db.Column(db.Float, default=1.0)
    image = db.Column(db.String(255), nullable=True)

    def get_modifiers(self):
        return {
            'attack': self.attack_modifier,
            'defense': self.defense_modifier,
            'dodge': self.dodge_modifier
        }