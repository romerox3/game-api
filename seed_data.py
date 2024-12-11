from flask import Flask
from models import db, Character, Item, Attack, Environment, User, CharacterImage
from seeds import seed_all
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def seed_database():
    with app.app_context():
        db.create_all()
        seed_all()

if __name__ == '__main__':
    seed_database()