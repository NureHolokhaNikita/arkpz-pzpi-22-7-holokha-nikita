from flask import jsonify

class PlantResponse:
    @staticmethod
    def response_all_plants(records):
        plants_data = [
            {
                "plant_id": record.plant_id,
                "user_id": record.user_id,
                "name": record.name,
                "added_at": record.added_at
            } for record in records
        ]
        return jsonify(plants_data), 200

    @staticmethod
    def response_plant(record):
        if not record:
            return jsonify({"error": "Plant not found"}), 404

        plant_data = {
            "plant_id": record.plant_id,
            "user_id": record.user_id,
            "name": record.name,
            "added_at": record.added_at
        }
        return jsonify(plant_data), 200
