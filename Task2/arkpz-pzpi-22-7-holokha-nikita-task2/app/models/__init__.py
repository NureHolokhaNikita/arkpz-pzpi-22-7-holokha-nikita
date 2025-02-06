from flask_sqlalchemy import SQLAlchemy

# Ініціалізація бази даних
db = SQLAlchemy()

# Імпорт всіх моделей
from .user import User
from .user_settings import UserSettings
from .plant import Plant
from .plant_catalog import PlantCatalog
from .sensor import Sensor
from .sensor_data import SensorData
from .threshold import Threshold
from .device import Device
from .schedule import Schedule
from .plant_care_history import PlantCareHistory
from .notification import Notification

# Функція для ініціалізації бази даних
def init_db(app):
    """Функція ініціалізації бази даних."""
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Створення всіх таблиць у базі
        print("✅ Database initialized successfully!")
