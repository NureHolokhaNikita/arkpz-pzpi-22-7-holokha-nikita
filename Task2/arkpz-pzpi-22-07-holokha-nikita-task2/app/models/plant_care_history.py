from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from datetime import datetime
from app.responses.plant_care_history_response import PlantCareHistoryResponse
from app.utils.error_handler import ErrorHandler

class PlantCareHistory(db.Model):
    __tablename__ = "plant_care_history"

    care_action_id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plant.plant_id'), nullable=False)
    action_type = Column(String(255), nullable=False)
    action_ts = Column(DateTime, default=datetime.utcnow)
    comment = Column(Text)

    @staticmethod
    def get_all_care_history():
        history = PlantCareHistory.query.all()
        return PlantCareHistoryResponse.response_all_care_history(history)

    @staticmethod
    def get_care_history_by_plant(plant_id):
        history = PlantCareHistory.query.filter_by(plant_id=plant_id).all()
        return PlantCareHistoryResponse.response_care_history_for_plant(history)

    @staticmethod
    def add_care_history_entry(data):
        try:
            new_entry = PlantCareHistory(
                plant_id=data.get("plant_id"),
                action_type=data.get("action_type"),
                action_ts=data.get("action_ts", datetime.utcnow()),  # Автоматично або передана дата
                comment=data.get("comment", "")
            )
            db.session.add(new_entry)
            db.session.commit()
            return {"message": "Care history entry added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add care history entry", 500)
