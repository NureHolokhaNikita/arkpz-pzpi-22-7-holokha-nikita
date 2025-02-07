from flask import jsonify

class NotificationResponse:
    @staticmethod
    def response_all_notifications(records):
        notifications_data = [
            {
                "notification_id": record.notification_id,
                "user_id": record.user_id,
                "message": record.message,
                "created_at": record.created_at,
                "is_processed": record.is_processed
            } for record in records
        ]
        return jsonify(notifications_data), 200

    @staticmethod
    def response_notification(record):
        if not record:
            return jsonify({"error": "Notification not found"}), 404

        notification_data = {
            "notification_id": record.notification_id,
            "user_id": record.user_id,
            "message": record.message,
            "created_at": record.created_at,
            "is_processed": record.is_processed
        }
        return jsonify(notification_data), 200
