from flask import jsonify

class UserResponse:
    @staticmethod
    def response_all_users(records):
        users_data = [
            {
                "user_id": record.user_id,
                "name": record.name,
                "email": record.email,
                "created_at": record.created_at
            } for record in records
        ]
        return jsonify(users_data), 200

    @staticmethod
    def response_user(record):
        if not record:
            return jsonify({"error": "User not found"}), 404

        user_data = {
            "user_id": record.user_id,
            "name": record.name,
            "email": record.email,
            "created_at": record.created_at
        }
        return jsonify(user_data), 200
