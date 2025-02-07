from app.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    from app.routes import user_bp, plant_bp, notification_bp, schedule_bp, sensor_bp, device_bp, threshold_bp, plant_catalog_bp, user_settings_bp, sensor_data_bp, plant_care_history_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(plant_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(sensor_bp)
    app.register_blueprint(device_bp)
    app.register_blueprint(threshold_bp)
    app.register_blueprint(plant_catalog_bp)
    app.register_blueprint(user_settings_bp)
    app.register_blueprint(sensor_data_bp)
    app.register_blueprint(plant_care_history_bp)

    with app.app_context():
        db.create_all()
    return app