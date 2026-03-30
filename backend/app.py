from flask import Flask, request, jsonify, redirect
from weather import get_weather
from spotify import (
    get_login_url,
    get_token,
    search_tracks,
    get_top_tracks,
    get_top_artists,
    get_recently_played
)
from recommender import weather_to_query, build_user_profile, build_personalized_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

spotify_access_token = None


@app.route("/")
def home():
    return """
    <h1>Spotify Weather App Backend</h1>
    <p><a href="/login">Login with Spotify</a></p>
    <p>Test weather route: <a href="/weather?city=Dallas">/weather?city=Dallas</a></p>
    <p>Test recommendations: <a href="/recommend?city=Dallas">/recommend?city=Dallas</a></p>
    """


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    result = get_weather(city)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)


@app.route("/login")
def login():
    return redirect(get_login_url())


@app.route("/callback")
def callback():
    global spotify_access_token

    code = request.args.get("code")

    if not code:
        return jsonify({"error": "No code returned from Spotify"}), 400

    token_info = get_token(code)

    if "access_token" not in token_info:
        return jsonify(token_info), 400

    spotify_access_token = token_info["access_token"]

    return """
    <h2>Spotify login successful.</h2>
    <p>You can now test recommendations at <a href="/recommend?city=Dallas">/recommend?city=Dallas</a></p>
    """


@app.route("/recommend", methods=["GET"])
def recommend():
    global spotify_access_token

    if not spotify_access_token:
        return jsonify({"error": "Please log in with Spotify first at /login"}), 401

    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    weather_data = get_weather(city)
    if "error" in weather_data:
        return jsonify(weather_data), 400

    top_artists = get_top_artists(spotify_access_token)
    top_tracks = get_top_tracks(spotify_access_token)
    recent_tracks = get_recently_played(spotify_access_token)

    user_profile = build_user_profile(top_artists, top_tracks, recent_tracks)
    query = build_personalized_query(weather_data["condition"], user_profile)

    spotify_results = search_tracks(spotify_access_token, query)

    print("Top artists:", top_artists)
    print("Top tracks:", top_tracks)
    print("Recent tracks:", recent_tracks)
    print("User profile:", user_profile)
    print("Query used:", query)

    tracks = []
    for item in spotify_results.get("tracks", {}).get("items", []):
        tracks.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"] if item["artists"] else "Unknown",
            "album": item["album"]["name"],
            "spotify_url": item["external_urls"]["spotify"]
        })

    return jsonify({
        "city": weather_data["city"],
        "condition": weather_data["condition"],
        "user_profile": user_profile,
        "query_used": query,
        "tracks": tracks
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)