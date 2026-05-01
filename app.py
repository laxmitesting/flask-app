from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_URL = "https://api.open-meteo.com/v1/forecast"

@app.route("/")
def home():
    return "Weather API is running"

@app.route("/weather")
def weather():
    latitude = request.args.get("lat", default=51.5074)   # London default
    longitude = request.args.get("lon", default=-0.1278)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(BASE_URL, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    return jsonify(data.get("current_weather", {}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)