import requests
from flask import current_app
import logging
import base64
from PIL import Image
import io
import os

logger = logging.getLogger(__name__)

class ItemGeneratorService:
    def __init__(self):
        self.base_url = current_app.config['ITEM_GENERATOR_URL']
        self.image_folder = current_app.config['UPLOAD_FOLDER']

    def generate_item(self, keyword):
        logger.info(f"Generando item con keyword: {keyword}")
        try:
            response = requests.post(f"{self.base_url}/api/generar-objeto", json={"palabra_clave": keyword})
            logger.info(f"Respuesta del servicio de generación: Status {response.status_code}")
            if response.status_code == 201:
                item_data = response.json()
                self.save_images_locally(item_data['object'], item_data['images'])
                return item_data['object']
            else:
                logger.error(f"Error en la respuesta del servicio: {response.text}")
                raise Exception(f"Error al generar el objeto: {response.text}")
        except requests.RequestException as e:
            logger.error(f"Error de conexión al servicio de generación: {str(e)}")
            raise Exception(f"Error de conexión al servicio de generación: {str(e)}")

    def save_images_locally(self, item_info, images):
        for image_type in ['no_bg', 'base', 'isolated']:
            base64_data = images[f'{image_type}_image']
            image_data = base64.b64decode(base64_data)
            image = Image.open(io.BytesIO(image_data))
            
            filename = f"{item_info['id']}_{image_type}.png"
            filepath = os.path.join(self.image_folder, filename)
            
            image.save(filepath)
            item_info[f'{image_type}_image_url'] = f"/images/{filename}"

item_generator_service = ItemGeneratorService()