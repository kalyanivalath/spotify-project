from flask import Flask, request, jsonify
from weather import get_weather

app = Flask(__name__)


@app.route("/")
def home():
    return "Spotify Weather App backend is running."


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    result = get_weather(city)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)