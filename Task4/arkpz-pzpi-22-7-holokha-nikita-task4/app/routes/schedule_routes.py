from flask import Blueprint, request
from app.models.schedule import Schedule

schedule_bp = Blueprint("schedule_bp", __name__)

@schedule_bp.route("/schedules", methods=["GET"])
def get_all_schedules():
    return Schedule.get_all_schedules()

@schedule_bp.route("/schedules/<int:schedule_id>", methods=["GET"])
def get_schedule(schedule_id):
    return Schedule.get_schedule_by_id(schedule_id)

@schedule_bp.route("/schedules", methods=["POST"])
def create_schedule():
    data = request.get_json()
    return Schedule.create_schedule(data)

@schedule_bp.route("/schedules/<int:schedule_id>", methods=["PUT"])
def update_schedule(schedule_id):
    data = request.get_json()
    return Schedule.update_schedule(schedule_id, data)

@schedule_bp.route("/schedules/<int:schedule_id>", methods=["DELETE"])
def delete_schedule(schedule_id):
    return Schedule.delete_schedule(schedule_id)
