from flask import Blueprint, request, jsonify
from models import Item, db, Aura, Character
from schemas import item_schema, aura_color_schema
from services.item_generator_service import ItemGeneratorService
from flask import make_response
import logging

item_bp = Blueprint('item', __name__)

logger = logging.getLogger(__name__)

@item_bp.route('/item', methods=['POST'])
def add_item():
    data = request.get_json()
    aura_color = Aura.query.get(data['aura_color_id'])
    new_item = Item(
        name=data['name'],
        description=data.get('description'),
        strength_bonus=data.get('strength_bonus', 0),
        defense_bonus=data.get('defense_bonus', 0),
        health_bonus=data.get('health_bonus', 0),
        dodge_bonus=data.get('dodge_bonus', 0),
        critical_chance_bonus=data.get('critical_chance_bonus', 0),
        aura_color=aura_color
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(item_schema.dump(new_item)), 201

@item_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify(item_schema.dump(items, many=True))

@item_bp.route('/aura_colors', methods=['GET'])
def get_aura_colors():
    aura_colors = Aura.query.all()
    return jsonify(aura_color_schema.dump(aura_colors, many=True))

@item_bp.route('/drop-item', methods=['POST', 'OPTIONS'])
def drop_item():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200

    logger.info("Recibida solicitud POST para drop_item")
    data = request.json
    logger.info(f"Datos recibidos: {data}")
    character_id = data.get('character_id')
    keyword = data.get('keyword')

    if not character_id or not keyword:
        logger.warning("Faltan character_id o keyword en la solicitud")
        return jsonify({"error": "Se requiere character_id y keyword"}), 400

    character = Character.query.get(character_id)
    if not character:
        logger.warning(f"No se encontró el personaje con id {character_id}")
        return jsonify({"error": "Personaje no encontrado"}), 404

    try:
        logger.info(f"Generando item con keyword: {keyword}")
        item_generator_service = ItemGeneratorService()
        item_data = item_generator_service.generate_item(keyword)
        logger.info(f"Item generado: {item_data}")
        
        new_item = Item(
            unique_id=item_data['unique_id'],
            name=item_data['name'],
            description=item_data['description'],
            item_type=item_data['item_type'],
            strength_bonus=item_data['strength_bonus'],
            defense_bonus=item_data['defense_bonus'],
            health_bonus=item_data['health_bonus'],
            dodge_bonus=item_data['dodge_bonus'],
            critical_chance_bonus=item_data['critical_chance_bonus'],
            agility_bonus=item_data['agility_bonus'],
            aura=item_data['aura'],
            no_bg_image_url=item_data['no_bg_image_url'],
            image_url=item_data['base_image_url']
        )
        
        character.items.append(new_item)
        db.session.add(new_item)
        db.session.commit()
        logger.info(f"Item creado y asociado al personaje: {new_item.to_dict()}")

        return jsonify({"message": "Item dropeado y asociado al personaje con éxito", "item": new_item.to_dict()}), 201
    except Exception as e:
        logger.error(f"Error al procesar drop_item: {str(e)}")
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@item_bp.route('/')
def serve_html():
    return send_from_directory('static', 'index.html')