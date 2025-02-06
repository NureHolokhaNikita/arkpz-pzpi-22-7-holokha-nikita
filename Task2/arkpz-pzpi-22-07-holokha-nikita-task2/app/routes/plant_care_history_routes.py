from flask import Blueprint, request
from app.models.plant_care_history import PlantCareHistory

plant_care_history_bp = Blueprint("plant_care_history_bp", __name__)

@plant_care_history_bp.route("/plant_care_history", methods=["GET"])
def get_all_plant_care_history():
    return PlantCareHistory.get_all_care_history()

@plant_care_history_bp.route("/plant_care_history/<int:plant_id>", methods=["GET"])
def get_care_history_by_plant(plant_id):
    return PlantCareHistory.get_care_history_by_plant(plant_id)

@plant_care_history_bp.route("/plant_care_history", methods=["POST"])
def create_care_history_entry():
    data = request.get_json()
    return PlantCareHistory.add_care_history_entry(data)
