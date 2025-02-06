from flask import Blueprint, request
from app.models.device import Device

device_bp = Blueprint("device_bp", __name__)

@device_bp.route("/devices", methods=["GET"])
def get_all_devices():
    return Device.get_all_devices()

@device_bp.route("/devices/<int:device_id>", methods=["GET"])
def get_device(device_id):
    return Device.get_device_by_id(device_id)

@device_bp.route("/devices", methods=["POST"])
def create_device():
    data = request.get_json()
    return Device.create_device(data)

@device_bp.route("/devices/<int:device_id>", methods=["PUT"])
def update_device(device_id):
    data = request.get_json()
    return Device.update_device(device_id, data)

@device_bp.route("/devices/<int:device_id>", methods=["DELETE"])
def delete_device(device_id):
    return Device.delete_device(device_id)
