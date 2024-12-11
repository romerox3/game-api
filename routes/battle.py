from flask import Blueprint, request, jsonify
from models.battle import Battle
from models.character import Character
from models.environment import Environment
from services.battle_service import BattleService
from schemas import battle_result_schema
from models import db

battle_bp = Blueprint('battle', __name__)

@battle_bp.route('/battle', methods=['POST'])
def start_battle():
    data = request.json
    character1 = Character.query.get(data['character1_id'])
    character2 = Character.query.get(data['character2_id'])
    
    environment = Environment.query.order_by(db.func.random()).first()
    
    if not character1 or not character2 or not environment:
        return jsonify({'error': 'Personajes o entorno no encontrados'}), 404

    battle = Battle(character1_id=character1.id, character2_id=character2.id, environment_id=environment.id)
    db.session.add(battle)
    db.session.commit()

    battle_service = BattleService(character1, character2, environment)
    result = battle_service.conduct_battle()

    battle.rounds = len(result.rounds)
    battle.result = result.winner
    db.session.commit()

    return jsonify(battle_result_schema.dump(result)), 200
