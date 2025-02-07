from flask import Blueprint, request
from app.models.sensor import Sensor

sensor_bp = Blueprint("sensor_bp", __name__)

@sensor_bp.route("/sensors", methods=["GET"])
def get_all_sensors():
    return Sensor.get_all_sensors()

@sensor_bp.route("/sensors/<int:sensor_id>", methods=["GET"])
def get_sensor_by_id(sensor_id):
    return Sensor.get_sensor_by_id(sensor_id)

@sensor_bp.route("/sensors", methods=["POST"])
def create_sensor():
    data = request.get_json()
    return Sensor.add_sensor(data)

@sensor_bp.route("/sensors/<int:sensor_id>", methods=["PUT"])
def update_sensor(sensor_id):
    data = request.get_json()
    return Sensor.update_sensor(sensor_id, data)

@sensor_bp.route("/sensors/<int:sensor_id>", methods=["DELETE"])
def delete_sensor(sensor_id):
    return Sensor.delete_sensor(sensor_id)
