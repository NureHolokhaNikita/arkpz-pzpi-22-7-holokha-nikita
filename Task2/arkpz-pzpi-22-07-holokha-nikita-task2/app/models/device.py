from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.utils.error_handler import ErrorHandler
from app.responses.device_response import DeviceResponse

class Device(db.Model):
    __tablename__ = "device"

    device_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    threshold_id = Column(Integer, ForeignKey('threshold.threshold_id'), nullable=True)
    schedule_id = Column(Integer, ForeignKey('schedule.schedule_id'), nullable=True)
    nickname = Column(String(255))
    device_type = Column(String(255))
    comment = Column(Text)

    user = relationship("User", backref="devices")
    threshold = relationship("Threshold", backref="devices")
    schedule = relationship("Schedule", backref="devices")

    def __repr__(self):
        return f"<Device {self.nickname}>"

    @staticmethod
    def get_all_devices():
        devices = Device.query.all()
        return DeviceResponse.response_all_devices(devices)

    @staticmethod
    def get_device_by_id(device_id):
        device = Device.query.get(device_id)
        return DeviceResponse.response_device(device)

    @staticmethod
    def create_device(data):
        try:
            new_device = Device(
                user_id=data.get("user_id"),
                threshold_id=data.get("threshold_id"),
                schedule_id=data.get("schedule_id"),
                nickname=data.get("nickname"),
                device_type=data.get("device_type"),
                comment=data.get("comment")
            )
            db.session.add(new_device)
            db.session.commit()
            return {"message": "Device added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add device", 500)

    @staticmethod
    def update_device(device_id, data):
        try:
            device = Device.query.get(device_id)
            if not device:
                return {"error": "Device not found"}, 404

            device.nickname = data.get("nickname", device.nickname)
            device.device_type = data.get("device_type", device.device_type)
            device.comment = data.get("comment", device.comment)
            db.session.commit()
            return {"message": "Device updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to update device", 500)

    @staticmethod
    def delete_device(device_id):
        try:
            device = Device.query.get(device_id)
            if not device:
                return {"error": "Device not found"}, 404

            db.session.delete(device)
            db.session.commit()
            return {"message": "Device deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to delete device", 500)
