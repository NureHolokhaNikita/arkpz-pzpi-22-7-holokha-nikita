from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.responses.sensor_response import SensorResponse
from app.utils.error_handler import ErrorHandler

class Sensor(db.Model):
    __tablename__ = "sensor"

    sensor_id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plant.plant_id"), nullable=False)
    sensor_type = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)

    plant = relationship("Plant", backref="sensors")

    def __repr__(self):
        return f"<Sensor {self.sensor_type} - {self.location}>"

    @staticmethod
    def get_all_sensors():
        sensors = Sensor.query.all()
        return SensorResponse.response_all_sensors(sensors)

    @staticmethod
    def get_sensor_by_id(sensor_id):
        sensor = Sensor.query.get(sensor_id)
        return SensorResponse.response_single_sensor(sensor)

    @staticmethod
    def add_sensor(data):
        try:
            new_sensor = Sensor(
                plant_id=data.get("plant_id"),
                sensor_type=data.get("sensor_type"),
                location=data.get("location"),
            )
            db.session.add(new_sensor)
            db.session.commit()
            return {"sensor_id": new_sensor.sensor_id, "message": "Sensor added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add sensor", 500)

    @staticmethod
    def update_sensor(sensor_id, data):
        sensor = Sensor.query.get(sensor_id)
        if not sensor:
            return {"error": "Sensor not found"}, 404

        sensor.plant_id = data.get("plant_id", sensor.plant_id)
        sensor.sensor_type = data.get("sensor_type", sensor.sensor_type)
        sensor.location = data.get("location", sensor.location)

        db.session.commit()
        return {"message": "Sensor updated successfully"}, 200

    @staticmethod
    def delete_sensor(sensor_id):
        sensor = Sensor.query.get(sensor_id)
        if not sensor:
            return {"error": "Sensor not found"}, 404

        db.session.delete(sensor)
        db.session.commit()
        return {"message": "Sensor deleted successfully"}, 200
