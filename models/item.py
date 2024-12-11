from . import db
import uuid

class Aura(db.Model):
    __tablename__ = 'aura'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    multiplier = db.Column(db.Float, nullable=False, default=1.0)
    description = db.Column(db.Text)
    color_hex = db.Column(db.String(7), nullable=False)

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.Text, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    item_type = db.Column(db.String(50))  # Añadimos este campo
    strength_bonus = db.Column(db.Integer, default=0)
    defense_bonus = db.Column(db.Integer, default=0)
    health_bonus = db.Column(db.Integer, default=0)
    dodge_bonus = db.Column(db.Float, default=0)
    critical_chance_bonus = db.Column(db.Float, default=0)
    agility_bonus = db.Column(db.Integer, default=0)  # Añadimos este campo
    aura = db.Column(db.String(50))  # Añadimos este campo
    no_bg_image_url = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)

    character = db.relationship('Character', back_populates='items')
    attacks = db.relationship('Attack', back_populates='item')

    @property
    def aura_multiplier(self):
        return self.aura.multiplier if self.aura else 1.0

    @property
    def effective_strength_bonus(self):
        return int(self.strength_bonus * self.aura_multiplier)

    @property
    def effective_defense_bonus(self):
        return int(self.defense_bonus * self.aura_multiplier)

    @property
    def effective_health_bonus(self):
        return int(self.health_bonus * self.aura_multiplier)

    @property
    def effective_dodge_bonus(self):
        return self.dodge_bonus * self.aura_multiplier

    @property
    def effective_critical_chance_bonus(self):
        return self.critical_chance_bonus * self.aura_multiplier

    def to_dict(self):
        return {
            'id': self.id,
            'unique_id': self.unique_id,
            'name': self.name,
            'description': self.description,
            'item_type': self.item_type,
            'strength_bonus': self.strength_bonus,
            'defense_bonus': self.defense_bonus,
            'health_bonus': self.health_bonus,
            'dodge_bonus': self.dodge_bonus,
            'critical_chance_bonus': self.critical_chance_bonus,
            'agility_bonus': self.agility_bonus,
            'aura': self.aura,
            'image_url': self.image_url,
            'no_bg_image_url': self.no_bg_image_url
        }

class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    base_damage = db.Column(db.Integer, nullable=False)
    critical_multiplier = db.Column(db.Float, default=2.0)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    item = db.relationship('Item', back_populates='attacks')