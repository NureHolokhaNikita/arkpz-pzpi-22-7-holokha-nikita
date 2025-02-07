from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.responses.plant_response import PlantResponse
from app.utils.error_handler import ErrorHandler

class Plant(db.Model):
    __tablename__ = "plant"

    plant_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    plant_type_id = Column(Integer, ForeignKey('plant_catalog.plant_type_id'))
    name = Column(String(255), nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Plant {self.name}>"

    @staticmethod
    def get_all_plants():
        plants = Plant.query.all()
        return PlantResponse.response_all_plants(plants)

    @staticmethod
    def get_plant_by_id(plant_id):
        plant = Plant.query.get(plant_id)
        return PlantResponse.response_plant(plant)

    @staticmethod
    def create_plant(data):
        try:
            new_plant = Plant(
                user_id=data.get("user_id"),
                plant_type_id=data.get("plant_type_id"),
                name=data.get("name"),
            )
            db.session.add(new_plant)
            db.session.commit()
            return {"message": "Plant added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to create plant", 500)

    @staticmethod
    def update_plant(plant_id, data):
        try:
            plant = Plant.query.get(plant_id)
            if not plant:
                return {"error": "Plant not found"}, 404

            plant.name = data.get("name", plant.name)
            db.session.commit()
            return {"message": "Plant updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to update plant", 500)

    @staticmethod
    def delete_plant(plant_id):
        try:
            plant = Plant.query.get(plant_id)
            if not plant:
                return {"error": "Plant not found"}, 404

            db.session.delete(plant)
            db.session.commit()
            return {"message": "Plant deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to delete plant", 500)
