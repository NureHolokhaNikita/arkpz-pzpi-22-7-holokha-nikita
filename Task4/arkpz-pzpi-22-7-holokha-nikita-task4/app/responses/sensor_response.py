from flask import jsonify

class SensorResponse:
    @staticmethod
    def response_all_sensors(records):
        sensors_data = [
            {
                "sensor_id": record.sensor_id,
                "plant_id": record.plant_id,
                "sensor_type": record.sensor_type,
                "location": record.location
            } for record in records
        ]
        return jsonify(sensors_data), 200

    @staticmethod
    def response_sensor(record):
        if not record:
            return jsonify({"error": "Sensor not found"}), 404

        sensor_data = {
            "sensor_id": record.sensor_id,
            "plant_id": record.plant_id,
            "sensor_type": record.sensor_type,
            "location": record.location
        }
        return jsonify(sensor_data), 200
