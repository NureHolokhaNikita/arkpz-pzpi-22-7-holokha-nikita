from flask import Blueprint, request
from app.models.sensor_data import SensorData

sensor_data_bp = Blueprint("sensor_data_bp", __name__)

@sensor_data_bp.route("/sensor_data/<int:sensor_id>", methods=["GET"])
def get_sensor_data(sensor_id):
    return SensorData.get_sensor_data(sensor_id)

@sensor_data_bp.route("/sensor_data", methods=["POST"])
def create_sensor_data():
    data = request.get_json()
    return SensorData.add_sensor_data(data)
