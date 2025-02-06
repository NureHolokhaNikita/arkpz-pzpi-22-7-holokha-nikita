from flask import jsonify

class DeviceResponse:
    @staticmethod
    def response_all_devices(records):
        devices = [
            {
                "device_id": record.device_id,
                "user_id": record.user_id,
                "threshold_id": record.threshold_id,
                "schedule_id": record.schedule_id,
                "nickname": record.nickname,
                "device_type": record.device_type,
                "comment": record.comment
            } for record in records
        ]
        return jsonify(devices), 200

    @staticmethod
    def response_device(record):
        if not record:
            return jsonify({"error": "Device not found"}), 404

        device_data = {
            "device_id": record.device_id,
            "user_id": record.user_id,
            "threshold_id": record.threshold_id,
            "schedule_id": record.schedule_id,
            "nickname": record.nickname,
            "device_type": record.device_type,
            "comment": record.comment
        }
        return jsonify(device_data), 200
