from flask import jsonify

class PlantCareHistoryResponse:
    @staticmethod
    def response_all_care_history(records):
        history = [
            {
                "care_action_id": record.care_action_id,
                "plant_id": record.plant_id,
                "action_type": record.action_type,
                "action_ts": record.action_ts.strftime("%Y-%m-%d %H:%M:%S"),
                "comment": record.comment
            } for record in records
        ]
        return jsonify(history), 200

    @staticmethod
    def response_care_history_for_plant(records):
        history = [
            {
                "care_action_id": record.care_action_id,
                "plant_id": record.plant_id,
                "action_type": record.action_type,
                "action_ts": record.action_ts.strftime("%Y-%m-%d %H:%M:%S"),
                "comment": record.comment
            } for record in records
        ]
        return jsonify(history), 200
