from app import db
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from app.responses.sensor_data_response import SensorDataResponse
from app.utils.error_handler import ErrorHandler

class SensorData(db.Model):
    __tablename__ = "sensor_data"

    sensor_data_id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensor.sensor_id'), nullable=False)
    measurement_value = Column(Float, nullable=False)
    measurement_time = Column(DateTime, default=datetime.utcnow)

    @staticmethod
    def get_sensor_data(sensor_id):
        data = SensorData.query.filter_by(sensor_id=sensor_id).all()
        return SensorDataResponse.response_sensor_data(data)

    @staticmethod
    def add_sensor_data(data):
        try:
            new_sensor_data = SensorData(
                sensor_id=data.get("sensor_id"),
                measurement_value=data.get("measurement_value"),
                measurement_time=data.get("measurement_time", datetime.utcnow())  # Дата може бути передана або встановлена автоматично
            )
            db.session.add(new_sensor_data)
            db.session.commit()
            return {"message": "Sensor data added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add sensor data", 500)
