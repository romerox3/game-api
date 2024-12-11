def register_blueprints(app):
    from .user import user_bp
    from .character import character_bp
    from .battle import battle_bp
    from .images import image_bp
    from .item import item_bp
    
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(character_bp, url_prefix='/api')
    app.register_blueprint(battle_bp, url_prefix='/api')
    app.register_blueprint(image_bp, url_prefix='/api')
    app.register_blueprint(item_bp, url_prefix='/api')