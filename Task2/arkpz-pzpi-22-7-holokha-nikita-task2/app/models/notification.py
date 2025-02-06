from app import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from datetime import datetime
from app.utils.error_handler import ErrorHandler
from app.responses.notification_response import NotificationResponse

class Notification(db.Model):
    __tablename__ = "notification"

    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_processed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Notification {self.notification_id}>"

    @staticmethod
    def get_all_notifications():
        notifications = Notification.query.all()
        return NotificationResponse.response_all_notifications(notifications)

    @staticmethod
    def get_notification_by_id(notification_id):
        notification = Notification.query.get(notification_id)
        return NotificationResponse.response_notification(notification)

    @staticmethod
    def create_notification(data):
        try:
            new_notification = Notification(
                user_id=data.get("user_id"),
                message=data.get("message"),
                is_processed=data.get("is_processed", False)
            )
            db.session.add(new_notification)
            db.session.commit()
            return {"message": "Notification created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to create notification", 500)

    @staticmethod
    def update_notification(notification_id, data):
        try:
            notification = Notification.query.get(notification_id)
            if not notification:
                return {"error": "Notification not found"}, 404

            notification.message = data.get("message", notification.message)
            notification.is_processed = data.get("is_processed", notification.is_processed)
            db.session.commit()
            return {"message": "Notification updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to update notification", 500)

    @staticmethod
    def delete_notification(notification_id):
        try:
            notification = Notification.query.get(notification_id)
            if not notification:
                return {"error": "Notification not found"}, 404

            db.session.delete(notification)
            db.session.commit()
            return {"message": "Notification deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to delete notification", 500)
