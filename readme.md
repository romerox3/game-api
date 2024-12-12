# Legendary Forge

API REST desarrollada en Flask para gestionar la lógica del juego Legendary Forge.

## Descripción

Esta API proporciona los endpoints necesarios para:
- Gestión de personajes
- Sistema de combate
- Gestión de items y equipamiento
- Sistema de entornos que afectan las batallas
- Generación procedural de items

## Tecnologías Principales

- Python 3.10+
- Flask 3.0.2
- SQLAlchemy + PostgreSQL
- Flask-Migrate para migraciones de base de datos
- Flask-Marshmallow para serialización
- Docker para contenerización

## Estructura del Proyecto

game_api/
├── app.py # Punto de entrada de la aplicación
├── config.py # Configuraciones
├── models/ # Modelos de datos
│ ├── init.py
│ ├── battle.py
│ ├── character.py
│ ├── environment.py
│ ├── item.py
│ └── user.py
├── routes/ # Endpoints de la API
│ ├── init.py
│ ├── battle.py
│ ├── character.py
│ ├── images.py
│ └── item.py
├── services/ # Lógica de negocio
├── schemas/ # Esquemas de serialización
├── migrations/ # Migraciones de base de datos
└── static/ # Archivos estáticos

## Instalación y Ejecución

### Prerrequisitos
- Docker y Docker Compose
- Python 3.10 o superior
- Poetry para gestión de dependencias

## Endpoints de la API

### Autenticación
- No implementada en esta versión

### Personajes
- `POST /characters`
  - Crear nuevo personaje
  - Body: 
    ```json
    {
      "name": "string",
      "user_id": "integer",
      "strength": "integer",
      "defense": "integer",
      "agility": "integer",
      "health": "integer",
      "mana": "integer"
    }
    ```

- `GET /characters`
  - Listar todos los personajes

- `GET /characters/<user_id>`
  - Obtener personaje por ID de usuario

### Batallas
- `POST /battle`
  - Iniciar batalla entre dos personajes
  - Body:
    ```json
    {
      "character1_id": "integer",
      "character2_id": "integer"
    }
    ```

### Items
- `POST /drop-item`
  - Generar y asignar nuevo item
  - Body:
    ```json
    {
      "character_id": "integer",
      "keyword": "string"
    }
    ```

- `GET /items`
  - Listar todos los items

- `GET /aura_colors`
  - Obtener colores de aura disponibles


### Modelos Principales

- **User**: Gestión de usuarios
- **Character**: Personajes del juego
- **Item**: Items y equipamiento
- **Battle**: Registro de batallas
- **Environment**: Entornos de batalla
