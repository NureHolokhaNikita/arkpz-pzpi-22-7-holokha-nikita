from flask import jsonify

class PlantCatalogResponse:
    @staticmethod
    def response_all_plant_catalog(records):
        plants = [
            {
                "plant_type_id": record.plant_type_id,
                "name": record.name,
                "recommended_temperature_range": record.recommended_temperature_range,
                "recommended_humidity_range": record.recommended_humidity_range,
                "watering_frequency": record.watering_frequency,
                "description": record.description
            } for record in records
        ]
        return jsonify(plants), 200

    @staticmethod
    def response_single_plant(record):
        if not record:
            return jsonify({"error": "Plant type not found"}), 404

        plant_data = {
            "plant_type_id": record.plant_type_id,
            "name": record.name,
            "recommended_temperature_range": record.recommended_temperature_range,
            "recommended_humidity_range": record.recommended_humidity_range,
            "watering_frequency": record.watering_frequency,
            "description": record.description
        }
        return jsonify(plant_data), 200
