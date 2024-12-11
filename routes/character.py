from flask import Blueprint, request, jsonify
from models import db, Character, User
from schemas import character_schema
import logging

logger = logging.getLogger(__name__)

character_bp = Blueprint('character', __name__)

@character_bp.route('/characters', methods=['POST'])
def create_character():
    print(request.json.get('user_id'))
    user_id = request.json.get('user_id')
    if not (user := User.query.get(user_id)):
        print(user)
        return jsonify({'message': 'Usuario no encontrado.'}), 404

    if user.character:
        return jsonify({'message': 'Este usuario ya tiene un personaje.'}), 400
    
    new_character = Character(
        name=request.json.get('name'),
        strength=request.json.get('strength', 10),
        defense=request.json.get('defense', 10),
        agility=request.json.get('agility', 10),
        health=request.json.get('health', 100),
        mana=request.json.get('mana', 50),
        critical_chance=request.json.get('critical_chance', 0.1),
        dodge_chance=request.json.get('dodge_chance', 0.1),
        user=user
    )
    db.session.add(new_character)
    db.session.commit()
    return jsonify({'message': 'Personaje creado con éxito.'}), 201


@character_bp.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    characters_serialized = [
        {
            'id': character.id,
            'name': character.name,
            'strength': character.strength,
            'defense': character.defense,
            'agility': character.agility,
            'health': character.health,
            'mana': character.mana,
            'critical_chance': character.critical_chance,
            'dodge_chance': character.dodge_chance,
            'user_id': character.user_id,
            'image': character.image.url,
            'items': character.items
        } for character in characters
    ]
    return jsonify(characters_serialized)

@character_bp.route('/characters/<int:user_id>', methods=['GET'])
def get_character(user_id):
    logger.info(f"Buscando personaje para el usuario con ID: {user_id}")
    if (user := User.query.filter_by(id=user_id).first()) and user.characters:
        character = user.characters[0]
        logger.info(f"Personaje encontrado: {character}")
        serialized_character = character_schema.dump(character)
        logger.info(f"Personaje serializado: {serialized_character}")
        return jsonify(serialized_character)
    return jsonify({'message': 'Character not found'}), 404
