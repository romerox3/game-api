from flask_marshmallow import Marshmallow
from models import Item, Attack, Battle, Environment, Aura, Character

ma = Marshmallow()

class AuraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Aura

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        include_fk = True

class AttackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attack

class EnvironmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Environment

class CharacterActionSchema(ma.Schema):
    attack = ma.Nested(AttackSchema, allow_none=True)
    available_attacks = ma.Nested(AttackSchema, many=True, allow_none=True)
    available_items = ma.Nested(ItemSchema, many=True, allow_none=True)

    class Meta:
        fields = ("name", "action", "initial_hp", "hp", "is_attacker", "attack", "attack_strength", "defense_success", "agility", "defense", "modifiers", "emotional_state", "available_attacks", "available_items")

class RoundSchema(ma.Schema):
    character1 = ma.Nested(CharacterActionSchema)
    character2 = ma.Nested(CharacterActionSchema)
    environment = ma.Nested(EnvironmentSchema)

    class Meta:
        fields = ("number", "character1", "character2", "damage", "narrative", "environment", "emotional_state")

class CharacterInfoSchema(ma.Schema):
    name = ma.Str()
    image = ma.Str()
    initial_hp = ma.Int()
    final_hp = ma.Int()
    strength = ma.Int()
    defense = ma.Int()
    agility = ma.Int()
    health = ma.Int()
    max_health = ma.Int()
    mana = ma.Int()
    max_mana = ma.Int()
    critical_chance = ma.Float()
    dodge_chance = ma.Float()
    attacks = ma.List(ma.Nested(AttackSchema))
    items = ma.List(ma.Nested(ItemSchema))

class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character
        include_fk = True
    
    items = ma.Nested(ItemSchema, many=True)
    attacks = ma.Nested(AttackSchema, many=True)
    image = ma.Method("get_image_url")

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None

class BattleResultSchema(ma.Schema):
    character1 = ma.Nested(CharacterInfoSchema)
    character2 = ma.Nested(CharacterInfoSchema)
    rounds = ma.List(ma.Nested(RoundSchema))

    class Meta:
        fields = ("character1", "character2", "rounds", "winner")

# Instancias de los esquemas
item_schema = ItemSchema()
aura_color_schema = AuraSchema()
attack_schema = AttackSchema()
environment_schema = EnvironmentSchema()
character_action_schema = CharacterActionSchema()
round_schema = RoundSchema()
battle_result_schema = BattleResultSchema()
character_schema = CharacterSchema()

# Puedes agregar más esquemas si es necesario