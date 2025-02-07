from flask import Blueprint

from .user_routes import user_bp
from .plant_routes import plant_bp
from .sensor_routes import sensor_bp
from .threshold_routes import threshold_bp
from .device_routes import device_bp
from .schedule_routes import schedule_bp
from .notification_routes import notification_bp
from .plant_catalog_routes import plant_catalog_bp
from app.routes.user_settings_routes import user_settings_bp
from app.routes.sensor_data_routes import sensor_data_bp
from app.routes.plant_care_history_routes import plant_care_history_bp
routes_bp = Blueprint("routes_bp", __name__)

routes_bp.register_blueprint(user_bp, url_prefix="/api")
routes_bp.register_blueprint(plant_bp, url_prefix="/api")
routes_bp.register_blueprint(sensor_bp, url_prefix="/api")
routes_bp.register_blueprint(threshold_bp, url_prefix="/api")
routes_bp.register_blueprint(device_bp, url_prefix="/api")
routes_bp.register_blueprint(schedule_bp, url_prefix="/api")
routes_bp.register_blueprint(notification_bp, url_prefix="/api")
routes_bp.register_blueprint(plant_catalog_bp, url_prefix="/api")
routes_bp.register_blueprint(user_settings_bp, url_prefix="/api")
routes_bp.register_blueprint(sensor_data_bp, url_prefix="/api")
routes_bp.register_blueprint(plant_care_history_bp, url_prefix="/api")
