from flask import jsonify

class ScheduleResponse:
    @staticmethod
    def response_all_schedules(records):
        schedules = [
            {
                "schedule_id": record.schedule_id,
                "user_id": record.user_id,
                "cron_expression": record.cron_expression,
                "action_type": record.action_type,
                "is_active": record.is_active
            } for record in records
        ]
        return jsonify(schedules), 200

    @staticmethod
    def response_schedule(record):
        if not record:
            return jsonify({"error": "Schedule not found"}), 404

        schedule_data = {
            "schedule_id": record.schedule_id,
            "user_id": record.user_id,
            "cron_expression": record.cron_expression,
            "action_type": record.action_type,
            "is_active": record.is_active
        }
        return jsonify(schedule_data), 200
