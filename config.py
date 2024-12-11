import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@db:5432/game'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEM_GENERATOR_URL = os.environ.get('ITEM_GENERATOR_URL') or 'http://item_generator_api:5001'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_segura'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
