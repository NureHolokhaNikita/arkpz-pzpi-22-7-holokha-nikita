from flask import jsonify

class ThresholdResponse:
    @staticmethod
    def response_all_thresholds(records):
        """Повертає список всіх порогових значень"""
        thresholds = [
            {
                "threshold_id": record.threshold_id,
                "sensor_id": record.sensor_id,
                "parameter": record.parameter,
                "name": record.name,
                "min_value": record.min_value,
                "max_value": record.max_value,
                "severity": record.severity,
                "is_active": record.is_active
            } for record in records
        ]
        return jsonify(thresholds), 200

    @staticmethod
    def response_single_threshold(record):
        """Повертає інформацію про порогове значення"""
        if not record:
            return jsonify({"error": "Threshold not found"}), 404

        threshold_data = {
            "threshold_id": record.threshold_id,
            "sensor_id": record.sensor_id,
            "parameter": record.parameter,
            "name": record.name,
            "min_value": record.min_value,
            "max_value": record.max_value,
            "severity": record.severity,
            "is_active": record.is_active
        }
        return jsonify(threshold_data), 200
