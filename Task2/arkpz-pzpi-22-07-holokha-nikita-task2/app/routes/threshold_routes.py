from flask import Blueprint, request
from app.models.threshold import Threshold

threshold_bp = Blueprint("threshold_bp", __name__)

@threshold_bp.route("/thresholds", methods=["GET"])
def get_all_thresholds():
    return Threshold.get_all_thresholds()

@threshold_bp.route("/thresholds/<int:threshold_id>", methods=["GET"])
def get_threshold_by_id(threshold_id):
    return Threshold.get_threshold_by_id(threshold_id)

@threshold_bp.route("/thresholds", methods=["POST"])
def create_threshold():
    data = request.get_json()
    return Threshold.add_threshold(data)

@threshold_bp.route("/thresholds/<int:threshold_id>", methods=["PUT"])
def update_threshold(threshold_id):
    data = request.get_json()
    return Threshold.update_threshold(threshold_id, data)

@threshold_bp.route("/thresholds/<int:threshold_id>", methods=["DELETE"])
def delete_threshold(threshold_id):
    return Threshold.delete_threshold(threshold_id)
