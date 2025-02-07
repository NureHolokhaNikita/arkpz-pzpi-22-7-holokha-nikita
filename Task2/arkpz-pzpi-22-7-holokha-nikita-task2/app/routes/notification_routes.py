from flask import Blueprint, request
from app.models.notification import Notification

notification_bp = Blueprint("notification_bp", __name__)

@notification_bp.route("/notifications", methods=["GET"])
def get_all_notifications():
    return Notification.get_all_notifications()

@notification_bp.route("/notifications/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):
    return Notification.get_notification_by_id(notification_id)

@notification_bp.route("/notifications", methods=["POST"])
def create_notification():
    data = request.get_json()
    return Notification.create_notification(data)

@notification_bp.route("/notifications/<int:notification_id>", methods=["PUT"])
def update_notification(notification_id):
    data = request.get_json()
    return Notification.update_notification(notification_id, data)

@notification_bp.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    return Notification.delete_notification(notification_id)
