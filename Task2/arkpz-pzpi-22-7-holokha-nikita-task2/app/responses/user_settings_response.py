from flask import jsonify

class UserSettingsResponse:
    @staticmethod
    def response_all_settings(records):
        """Повертає список всіх налаштувань користувачів"""
        settings = [
            {
                "user_settings_id": record.user_settings_id,
                "user_id": record.user_id,
                "notification_preferences": record.notification_preferences,
                "language": record.preferred_language,
                "timezone": record.timezone
            } for record in records
        ]
        return jsonify(settings), 200

    @staticmethod
    def response_single_settings(record):
        """Повертає інформацію про налаштування одного користувача"""
        if not record:
            return jsonify({"error": "User settings not found"}), 404

        settings_data = {
            "settings_id": record.settings_id,
            "user_id": record.user_id,
            "notification_preferences": record.notification_preferences,
            "language": record.preferred_language,
            "timezone": record.timezone
        }
        return jsonify(settings_data), 200
