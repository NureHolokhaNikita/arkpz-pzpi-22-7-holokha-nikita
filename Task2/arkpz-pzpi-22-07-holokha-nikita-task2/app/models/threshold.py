from app import db
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app.responses.threshold_response import ThresholdResponse
from app.utils.error_handler import ErrorHandler

class Threshold(db.Model):
    __tablename__ = "threshold"

    threshold_id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensor.sensor_id'), nullable=False)
    parameter = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    min_value = Column(Float)
    max_value = Column(Float)
    severity = Column(String(50))
    is_active = Column(Boolean, default=True)

    @staticmethod
    def get_all_thresholds():
        thresholds = Threshold.query.all()
        return ThresholdResponse.response_all_thresholds(thresholds)

    @staticmethod
    def get_threshold_by_id(threshold_id):
        threshold = Threshold.query.get(threshold_id)
        return ThresholdResponse.response_single_threshold(threshold)

    @staticmethod
    def add_threshold(data):
        try:
            new_threshold = Threshold(
                sensor_id=data.get("sensor_id"),
                parameter=data.get("parameter"),
                name=data.get("name"),
                min_value=data.get("min_value"),
                max_value=data.get("max_value"),
                severity=data.get("severity"),
                is_active=data.get("is_active", True)
            )
            db.session.add(new_threshold)
            db.session.commit()
            return {"message": "Threshold added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add threshold", 500)

    @staticmethod
    def update_threshold(threshold_id, data):
        threshold = Threshold.query.get(threshold_id)
        if not threshold:
            return {"error": "Threshold not found"}, 404

        threshold.sensor_id = data.get("sensor_id", threshold.sensor_id)
        threshold.parameter = data.get("parameter", threshold.parameter)
        threshold.name = data.get("name", threshold.name)
        threshold.min_value = data.get("min_value", threshold.min_value)
        threshold.max_value = data.get("max_value", threshold.max_value)
        threshold.severity = data.get("severity", threshold.severity)
        threshold.is_active = data.get("is_active", threshold.is_active)

        db.session.commit()
        return {"message": "Threshold updated successfully"}, 200

    @staticmethod
    def delete_threshold(threshold_id):
        threshold = Threshold.query.get(threshold_id)
        if not threshold:
            return {"error": "Threshold not found"}, 404

        db.session.delete(threshold)
        db.session.commit()
        return {"message": "Threshold deleted successfully"}, 200
