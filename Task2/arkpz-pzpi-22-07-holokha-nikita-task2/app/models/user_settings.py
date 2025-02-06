from app import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.responses.user_settings_response import UserSettingsResponse
from app.utils.error_handler import ErrorHandler

class UserSettings(db.Model):
    __tablename__ = "user_settings"

    user_settings_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False, unique=True)
    notification_preferences = Column(Boolean, default=True)
    language = Column(String(10), default="en")
    timezone = Column(String(10), default="UTC")

    user = relationship("User", backref="settings")

    def __repr__(self):
        return f"<UserSettings user_id={self.user_id} notifications={self.notification_preferences}>"

    @staticmethod
    def get_all_settings():
        settings = UserSettings.query.all()
        return UserSettingsResponse.response_all_settings(settings)

    @staticmethod
    def get_user_settings(user_id):
        settings = UserSettings.query.filter_by(user_id=user_id).first()
        return UserSettingsResponse.response_single_settings(settings)

    @staticmethod
    def add_user_settings(data):
        try:
            new_settings = UserSettings(
                user_id=data.get("user_id"),
                notification_preferences=data.get("notification_preferences", True),
                language=data.get("language", "en"),
                timezone=data.get("timezone", False)
            )
            db.session.add(new_settings)
            db.session.commit()
            return {"message": "User settings added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to add user settings", 500)

    @staticmethod
    def update_user_settings(user_id, data):
        settings = UserSettings.query.filter_by(user_id=user_id).first()
        if not settings:
            return {"error": "User settings not found"}, 404

        settings.notification_preferences = data.get("notification_preferences", settings.notification_preferences)
        settings.language = data.get("language", settings.language)
        settings.timezone = data.get("timezone", settings.timezone)

        db.session.commit()
        return {"message": "User settings updated successfully"}, 200

    @staticmethod
    def delete_user_settings(user_id):
        settings = UserSettings.query.filter_by(user_id=user_id).first()
        if not settings:
            return {"error": "User settings not found"}, 404

        db.session.delete(settings)
        db.session.commit()
        return {"message": "User settings deleted successfully"}, 200
