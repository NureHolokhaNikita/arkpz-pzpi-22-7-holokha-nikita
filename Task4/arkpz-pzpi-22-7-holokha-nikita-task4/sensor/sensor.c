#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// Піни сенсорів
#define DHT_PIN 2
#define DHT_TYPE DHT22
#define LDR_PIN 32
#define SOIL_MOISTURE_PIN 33

// Дані WiFi
#define WIFI_SSID "Wokwi-GUEST"
#define WIFI_PASS ""

// Сервер API
const char* registerURL = " http://7677-81-162-246-225.ngrok-free.app/sensors";
const char* sensorDataURL = " http://7677-81-162-246-225.ngrok-free.app/sensor_data";

DHT dht(DHT_PIN, DHT_TYPE);

// Сенсори та їх ID
int sensorIds[4];  
const char* sensorTypes[4] = { "Temperature", "Humidity", "Light", "Soil Moisture" };
const char* sensorLocations[4] = { "Living Room", "Living Room", "Near Window", "Plant Pot" };

void setup() {
    Serial.begin(115200);
    dht.begin();
    
    WiFi.begin(WIFI_SSID, WIFI_PASS);
    while (WiFi.status() != WL_CONNECTED) {
        Serial.println("Connecting to WiFi...");
        delay(1000);
    }
    Serial.println("WiFi Connected!");

    // Реєструємо всі сенсори
    for (int i = 0; i < 4; i++) {
        sensorIds[i] = registerSensor(1, sensorTypes[i], sensorLocations[i]);
    }
}

void loop() {
    float values[4] = {
        dht.readTemperature(),
        dht.readHumidity(),
        2048 - analogRead(LDR_PIN),
        map(analogRead(SOIL_MOISTURE_PIN), 0, 2048, 0, 100)
    };

    for (int i = 0; i < 4; i++) {
        if (sensorIds[i] > 0) {
            sendDataToServer(sensorIds[i], values[i]);
        } else {
            Serial.println("Error: Sensor ID not valid.");
        }
    }

    delay(5000);
}

// **Реєстрація сенсора**
int registerSensor(int plant_id, const char* type, const char* location) {
    if (WiFi.status() != WL_CONNECTED) return -1;

    HTTPClient http;
    http.begin(registerURL);
    http.addHeader("Content-Type", "application/json");

    String jsonData = String("{\"plant_id\":") + plant_id + ",\"sensor_type\":\"" + type + "\",\"location\":\"" + location + "\"}";

    int responseCode = http.POST(jsonData);
    String response = http.getString();
    http.end();

    Serial.print("Registering Sensor: ");
    Serial.println(type);
    Serial.print("Server Response Code: ");
    Serial.println(responseCode);
    Serial.print("Server Response: ");
    Serial.println(response);

    // **Парсимо JSON-відповідь**
    StaticJsonDocument<200> doc;
    DeserializationError error = deserializeJson(doc, response);

    if (error) {
        Serial.print("JSON Parsing Failed: ");
        Serial.println(error.c_str());
        return -1;
    }

    int sensorId = doc["sensor_id"];  // Отримуємо sensor_id з JSON
    return sensorId > 0 ? sensorId : -1;
}

// **Надсилання даних**
void sendDataToServer(int sensorId, float value) {
    if (WiFi.status() != WL_CONNECTED || sensorId <= 0) return;

    HTTPClient http;
    http.begin(sensorDataURL);
    http.addHeader("Content-Type", "application/json");

    String jsonData = String("{\"sensor_id\":") + sensorId + ",\"measurement_value\":" + value + "}";

    int responseCode = http.POST(jsonData);
    Serial.print("Sending Data to Sensor ID ");
    Serial.print(sensorId);
    Serial.print(", Value: ");
    Serial.println(value);
    Serial.print("Server Response Code: ");
    Serial.println(responseCode);

    http.end();
}
