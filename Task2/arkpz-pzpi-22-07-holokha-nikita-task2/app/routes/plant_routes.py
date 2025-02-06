from flask import Blueprint, request
from app.models.plant import Plant

plant_bp = Blueprint("plant_bp", __name__)

@plant_bp.route("/plants", methods=["GET"])
def get_all_plants():
    return Plant.get_all_plants()

@plant_bp.route("/plants/<int:plant_id>", methods=["GET"])
def get_plant(plant_id):
    return Plant.get_plant_by_id(plant_id)

@plant_bp.route("/plants", methods=["POST"])
def create_plant():
    data = request.get_json()
    return Plant.create_plant(data)

@plant_bp.route("/plants/<int:plant_id>", methods=["PUT"])
def update_plant(plant_id):
    data = request.get_json()
    return Plant.update_plant(plant_id, data)

@plant_bp.route("/plants/<int:plant_id>", methods=["DELETE"])
def delete_plant(plant_id):
    return Plant.delete_plant(plant_id)
