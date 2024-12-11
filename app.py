import os
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, init_db
from config import Config

ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    init_db(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    with app.app_context():
        from routes import register_blueprints
        register_blueprints(app)

    @app.errorhandler(415)
    def unsupported_media_type(error):
        return jsonify({"error": "Unsupported Media Type"}), 415

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)