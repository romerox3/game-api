from flask import Blueprint, request, jsonify
from models import db, User

image_bp = Blueprint('image', __name__)

@image_bp.route('/api/images', methods=['GET'])
def list_images():
    images = CharacterImage.query.all()
    return jsonify([{'id': img.id, 'url': img.url, 'description': img.description} for img in images])

@image_bp.route('/api/images', methods=['POST'])
def add_image():
    data = request.get_json()
    new_image = CharacterImage(url=data['url'], description=data.get('description'))
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'id': new_image.id, 'url': new_image.url}), 201

@image_bp.route('/api/images/<int:image_id>', methods=['DELETE'])
def delete_image(image_id):
    image = CharacterImage.query.get_or_404(image_id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image deleted'}), 204