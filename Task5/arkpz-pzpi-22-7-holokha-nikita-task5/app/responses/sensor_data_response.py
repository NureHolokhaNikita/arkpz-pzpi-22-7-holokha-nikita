from flask import jsonify

class SensorDataResponse:
    @staticmethod
    def response_sensor_data(records):
        data = [
            {
                "sensor_data_id": record.sensor_data_id,
                "sensor_id": record.sensor_id,
                "measurement_value": record.measurement_value,
                "measurement_time": record.measurement_time.strftime("%Y-%m-%d %H:%M:%S")
            } for record in records
        ]
        return jsonify(data), 200
