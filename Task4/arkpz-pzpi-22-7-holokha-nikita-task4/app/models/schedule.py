from app import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.utils.error_handler import ErrorHandler
from app.responses.schedule_response import ScheduleResponse
class Schedule(db.Model):
    __tablename__ = "schedule"

    schedule_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    cron_expression = Column(String(255), nullable=False)
    action_type = Column(String(255))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Schedule {self.schedule_id} - {self.cron_expression}>"

    @staticmethod
    def get_all_schedules():
        schedules = Schedule.query.all()
        return ScheduleResponse.response_all_schedules(schedules)

    @staticmethod
    def get_schedule_by_id(schedule_id):
        schedule = Schedule.query.get(schedule_id)
        return ScheduleResponse.response_schedule(schedule)

    @staticmethod
    def create_schedule(data):
        try:
            new_schedule = Schedule(
                user_id=data.get("user_id"),
                cron_expression=data.get("cron_expression"),
                action_type=data.get("action_type"),
                is_active=data.get("is_active", True)
            )
            db.session.add(new_schedule)
            db.session.commit()
            return {"message": "Schedule created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to create schedule", 500)

    @staticmethod
    def update_schedule(schedule_id, data):
        try:
            schedule = Schedule.query.get(schedule_id)
            if not schedule:
                return {"error": "Schedule not found"}, 404

            schedule.cron_expression = data.get("cron_expression", schedule.cron_expression)
            schedule.action_type = data.get("action_type", schedule.action_type)
            schedule.is_active = data.get("is_active", schedule.is_active)
            db.session.commit()
            return {"message": "Schedule updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to update schedule", 500)

    @staticmethod
    def delete_schedule(schedule_id):
        try:
            schedule = Schedule.query.get(schedule_id)
            if not schedule:
                return {"error": "Schedule not found"}, 404

            db.session.delete(schedule)
            db.session.commit()
            return {"message": "Schedule deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return ErrorHandler.handle_error(e, "Failed to delete schedule", 500)
