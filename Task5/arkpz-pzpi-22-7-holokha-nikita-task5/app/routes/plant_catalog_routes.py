from flask import Blueprint, request
from app.models.plant_catalog import PlantCatalog

plant_catalog_bp = Blueprint("plant_catalog_bp", __name__)

@plant_catalog_bp.route("/plant_catalog", methods=["GET"])
def get_all_plants():
    return PlantCatalog.get_all_catalog()

@plant_catalog_bp.route("/plant_catalog/<int:plant_type_id>", methods=["GET"])
def get_plant_by_id(plant_type_id):
    return PlantCatalog.get_plant_by_id(plant_type_id)

@plant_catalog_bp.route("/plant_catalog", methods=["POST"])
def create_plant_type():
    data = request.get_json()
    return PlantCatalog.add_plant_type(data)

@plant_catalog_bp.route("/plant_catalog/<int:plant_type_id>", methods=["PUT"])
def update_plant_type(plant_type_id):
    data = request.get_json()
    return PlantCatalog.update_plant_type(plant_type_id, data)

@plant_catalog_bp.route("/plant_catalog/<int:plant_type_id>", methods=["DELETE"])
def delete_plant_type(plant_type_id):
    return PlantCatalog.delete_plant_type(plant_type_id)
