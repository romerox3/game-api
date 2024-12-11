from . import db
from sqlalchemy.ext.hybrid import hybrid_property
from typing import Dict, List
import uuid

class CharacterImage(db.Model):
    __tablename__ = 'character_images'
    
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)

    character = db.relationship('Character', back_populates='image', uselist=False)

class Character(db.Model):
    __tablename__ = 'characters'
    
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('character_images.id'), nullable=True)
    name = db.Column(db.String(80), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    max_health = db.Column(db.Integer, nullable=False)
    mana = db.Column(db.Integer, nullable=False)
    max_mana = db.Column(db.Integer, nullable=False)
    base_strength = db.Column(db.Integer, nullable=False)
    base_defense = db.Column(db.Integer, nullable=False)
    base_agility = db.Column(db.Integer, nullable=False)
    critical_chance = db.Column(db.Float, nullable=False, default=0.1)
    dodge_chance = db.Column(db.Float, nullable=False, default=0.1)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    image = db.relationship('CharacterImage', back_populates='character')
    user = db.relationship('User', back_populates='characters', overlaps="owner")
    items = db.relationship('Item', back_populates='character')

    @hybrid_property
    def strength(self) -> int:
        return self.base_strength + sum(item.strength_bonus for item in self.items)

    @hybrid_property
    def defense(self) -> int:
        return self.base_defense + sum(item.defense_bonus for item in self.items)

    @hybrid_property
    def agility(self) -> int:
        return self.base_agility + sum(item.agility_bonus for item in self.items)

    @property
    def inventory(self) -> List[Dict]:
        return [item.to_dict() for item in self.items]

    @property
    def equipment(self) -> Dict[str, Dict]:
        return {item.slot: item.to_dict() for item in self.items}

    @property
    def equipped_items(self):
        return [item for item in self.items]

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)

    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        return False

    def recover_mana(self, amount):
        self.mana = min(self.mana + amount, self.max_mana)

    @property
    def health_percentage(self):
        return (self.health / self.max_health) * 100

    @property
    def mana_percentage(self):
        return (self.mana / self.max_mana) * 100

    def is_alive(self):
        return self.health > 0

    def increase_max_health(self, amount):
        self.max_health += amount
        self.health = min(self.health, self.max_health)

    def increase_max_mana(self, amount):
        self.max_mana += amount
        self.mana = min(self.mana, self.max_mana)
