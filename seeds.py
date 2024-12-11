from models import db, User, Character, Item, Attack, Environment, Aura, CharacterImage
import random
import uuid

# Lista de nombres antiguos reales de diferentes culturas
nombres_antiguos = [
    "Alejandro", "Cleopatra", "Julio", "Octavio", "Nerón", "Marco", "Aurelio", "Adriano", "Trajano", "Constantino",
    "Justiniano", "Teodora", "Atila", "Carlomagno", "Ragnar", "Guillermo", "Ricardo", "Saladino", "Gengis", "Kublai",
    "Tamerlán", "Isabel", "Fernando", "Moctezuma", "Atahualpa", "Akbar", "Solimán", "Iván", "Catalina", "Pedro",
    "Tutankamón", "Ramsés", "Nefertiti", "Ciro", "Darío", "Jerjes", "Nabucodonosor", "Hammurabi", "Gilgamesh", "Asurbanipal",
    "Pericles", "Sócrates", "Platón", "Aristóteles", "Pitágoras", "Arquímedes", "Hipócrates", "Heródoto", "Tucídides", "Homero",
    "Confucio", "Lao-Tsé", "Sun Tzu", "Qin Shi Huang", "Wu Zetian", "Hatshepsut", "Zenobia", "Boudica", "Hipatia", "Aspasia",
    "Aníbal", "Escipión", "Vercingétorix", "Arminio", "Atila", "Alarico", "Teodorico", "Clovis", "Carlomagno", "Rolando",
    "Leónidas", "Temístocles", "Pericles", "Alcibíades", "Epaminondas", "Filipo", "Ptolomeo", "Antígono", "Pirro", "Mitrídates"
]

def generar_nombre_aleatorio():
    return random.choice(nombres_antiguos)

def seed_environments():
    environments = [
        Environment(name="Bosque denso", description="Un bosque oscuro y frondoso", effect_type="advantageous", attack_modifier=1.1, defense_modifier=0.9, dodge_modifier=1.2, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/bosque.png"),
        Environment(name="Desierto árido", description="Un vasto desierto con arena ardiente", effect_type="disadvantageous", attack_modifier=1.2, defense_modifier=1.0, dodge_modifier=0.8, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/desierto.png"),
        Environment(name="Montaña escarpada", description="Altas montañas con terreno difícil", effect_type="advantageous", attack_modifier=0.9, defense_modifier=1.2, dodge_modifier=1.1, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/montaña.png"),
        Environment(name="Llanura abierta", description="Amplias praderas con hierba alta", effect_type="neutral", attack_modifier=1.0, defense_modifier=1.0, dodge_modifier=1.0, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/pradera.png"),
        Environment(name="Ruinas antiguas", description="Restos de una civilización antigua", effect_type="advantageous", attack_modifier=1.1, defense_modifier=1.1, dodge_modifier=1.0, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/Ancient-ruins.png"),
        Environment(name="Pantano brumoso", description="Un pantano húmedo y lleno de niebla", effect_type="disadvantageous", attack_modifier=0.9, defense_modifier=1.0, dodge_modifier=1.3, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/pantano.png"),
        Environment(name="Volcán activo", description="Un terreno peligroso con ríos de lava", effect_type="disadvantageous", attack_modifier=1.3, defense_modifier=0.8, dodge_modifier=1.1, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/volcan.png"),
        Environment(name="Caverna helada", description="Una cueva fría y resbaladiza", effect_type="neutral", attack_modifier=1.0, defense_modifier=1.2, dodge_modifier=0.9, image="https://raw.githubusercontent.com/romerox3/images/12ed49915825a169fc54f4b67acb13f3fc72c6a3/cueva.png")
    ]
    db.session.add_all(environments)
    db.session.commit()
    print("Entornos creados.")

def seed_aura_colors():
    auras = [
        {"name": "Ninguno", "multiplier": 1.0, "description": "Sin aura", "color_hex": "#FFFFFF"},
        {"name": "Rojo", "multiplier": 1.2, "description": "Aumenta el daño", "color_hex": "#FF0000"},
        {"name": "Azul", "multiplier": 1.15, "description": "Aumenta la defensa", "color_hex": "#0000FF"},
        {"name": "Verde", "multiplier": 1.1, "description": "Aumenta la salud", "color_hex": "#00FF00"},
        {"name": "Amarillo", "multiplier": 1.25, "description": "Aumenta la probabilidad de crítico", "color_hex": "#FFFF00"},
        {"name": "Púrpura", "multiplier": 1.3, "description": "Aumenta todos los stats ligeramente", "color_hex": "#800080"},
    ]
    
    for aura_data in auras:
        existing_aura = Aura.query.filter_by(name=aura_data['name']).first()
        if not existing_aura:
            new_aura = Aura(**aura_data)
            db.session.add(new_aura)
    
    db.session.commit()
    print("Colores de aura creados o actualizados.")
    return Aura.query.all()

def generate_aura():
    auras = Aura.query.all()
    return random.choice(auras) if auras else None

def seed_characters():
    user = User.query.first()
    if not user:
        user = User(username="usuario_prueba2", email="prueba2@ejemplo.com", password="contraseña123")
        db.session.add(user)
        db.session.commit()
        print("Usuario de prueba creado.")

    characters = []
    nombres_usados = set()
    for i in range(1, 11):
        nombre = generar_nombre_aleatorio()
        while nombre in nombres_usados:
            nombre = generar_nombre_aleatorio()
        nombres_usados.add(nombre)
        
        character = Character(
            name=nombre,
            health=random.randint(100, 150),
            max_health=random.randint(100, 150),
            mana=random.randint(50, 100),
            max_mana=random.randint(50, 100),
            base_strength=random.randint(10, 20),
            base_defense=random.randint(10, 20),
            base_agility=random.randint(10, 20),
            critical_chance=0.1,
            dodge_chance=random.uniform(0.05, 0.2),
            user_id=user.id,
            image=CharacterImage(url=f"https://ejemplo.com/imagen{i}.jpg")
        )
        characters.append(character)
    
    db.session.add_all(characters)
    db.session.flush()
    db.session.commit()
    print("Personajes creados")

def seed_all():
    seed_environments()
    seed_aura_colors()
    seed_characters()
    print("Base de datos poblada con éxito!")

if __name__ == "__main__":
    seed_all()