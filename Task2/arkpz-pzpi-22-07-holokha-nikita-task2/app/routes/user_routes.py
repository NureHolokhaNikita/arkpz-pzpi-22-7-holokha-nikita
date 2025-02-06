from flask import Blueprint, request
from app.models.user import User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    return User.get_all_users()

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return User.get_user_by_id(user_id)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return User.create_user(data)

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    return User.update_user(user_id, data)

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return User.delete_user(user_id)
