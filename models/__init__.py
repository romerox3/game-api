from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .character import Character, CharacterImage
from .environment import Environment
from .battle import Battle
from .item import Item, Attack, Aura


def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

