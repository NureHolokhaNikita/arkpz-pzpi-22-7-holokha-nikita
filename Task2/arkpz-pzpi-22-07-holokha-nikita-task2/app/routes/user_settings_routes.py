from flask import Blueprint, request
from app.models.user_settings import UserSettings

user_settings_bp = Blueprint("user_settings_bp", __name__)

@user_settings_bp.route("/user_settings", methods=["GET"])
def get_all_user_settings():
    return UserSettings.get_all_settings()

@user_settings_bp.route("/user_settings/<int:user_id>", methods=["GET"])
def get_user_settings(user_id):
    return UserSettings.get_user_settings(user_id)

@user_settings_bp.route("/user_settings", methods=["POST"])
def create_user_settings():
    data = request.get_json()
    return UserSettings.add_user_settings(data)

@user_settings_bp.route("/user_settings/<int:user_id>", methods=["PUT"])
def update_user_settings(user_id):
    data = request.get_json()
    return UserSettings.update_user_settings(user_id, data)

@user_settings_bp.route("/user_settings/<int:user_id>", methods=["DELETE"])
def delete_user_settings(user_id):
    return UserSettings.delete_user_settings(user_id)
