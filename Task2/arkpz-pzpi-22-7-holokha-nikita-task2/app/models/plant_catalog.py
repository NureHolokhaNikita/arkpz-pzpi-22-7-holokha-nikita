from app import db
from sqlalchemy import Column, Integer, String, Text
from app.responses.plant_catalog_response import PlantCatalogResponse
from app.utils.error_handler import ErrorHandler

class PlantCatalog(db.Model):
    __tablename__ = "plant_catalog"

    plant_type_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    recommended_temperature_range = Column(String(255))
    recommended_humidity_range = Column(String(255))
    watering_frequency = Column(String(255))
    description = Column(Text)

    def __repr__(self):
        return f"<PlantCatalog {self.name}>"

    @staticmethod
    def get_all_catalog():
        catalog = PlantCatalog.query.all()
        return PlantCatalogResponse.response_all_plant_catalog(catalog)

    @staticmethod
    def get_plant_by_id(plant_type_id):
        plant = PlantCatalog.query.get(plant_type_id)
        return PlantCatalogResponse.response_single_plant(plant)

    @staticmethod
    def add_plant_type(data):
        try:
            new_plant = PlantCatalog(
                name=data.get("name"),
                recommended_temperature_range=data.get("recommended_temperature_range"),
                recommended_humidity_range=data.get("recommended_humidity_range"),
                watering_frequency=data.get("watering_frequency"),
                description=data.get("description")
            )
            db.session.add(new_plant)
            db.session.commit()
            return {"message": "Plant type added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add plant type", 500)

    @staticmethod
    def update_plant_type(plant_type_id, data):
        plant = PlantCatalog.query.get(plant_type_id)
        if not plant:
            return {"error": "Plant type not found"}, 404

        plant.name = data.get("name", plant.name)
        plant.recommended_temperature_range = data.get("recommended_temperature_range", plant.recommended_temperature_range)
        plant.recommended_humidity_range = data.get("recommended_humidity_range", plant.recommended_humidity_range)
        plant.watering_frequency = data.get("watering_frequency", plant.watering_frequency)
        plant.description = data.get("description", plant.description)

        db.session.commit()
        return {"message": "Plant type updated successfully"}, 200

    @staticmethod
    def delete_plant_type(plant_type_id):
        plant = PlantCatalog.query.get(plant_type_id)
        if not plant:
            return {"error": "Plant type not found"}, 404

        db.session.delete(plant)
        db.session.commit()
        return {"message": "Plant type deleted successfully"}, 200
