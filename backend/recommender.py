def weather_to_query(condition):
    condition = condition.lower()

    if "sun" in condition or "clear" in condition:
        return "upbeat pop"
    elif "rain" in condition or "drizzle" in condition:
        return "chill acoustic"
    elif "cloud" in condition or "overcast" in condition:
        return "indie mellow"
    elif "snow" in condition:
        return "ambient calm"
    elif "storm" in condition or "thunder" in condition:
        return "dark electronic"
    else:
        return "feel good"


def build_user_profile(top_artists_data, top_tracks_data, recent_data=None):
    artists = []
    track_names = []

    for item in top_artists_data.get("items", [])[:5]:
        artists.append(item["name"])

    for item in top_tracks_data.get("items", [])[:5]:
        track_names.append(item["name"])

    recent_artists = []
    if recent_data:
        for item in recent_data.get("items", [])[:5]:
            track = item.get("track", {})
            for artist in track.get("artists", [])[:1]:
                recent_artists.append(artist["name"])

    return {
        "favorite_artists": artists,
        "favorite_tracks": track_names,
        "recent_artists": recent_artists
    }


def build_personalized_query(weather_condition, user_profile):
    mood = weather_to_query(weather_condition)

    artist_part = ""
    if user_profile["favorite_artists"]:
        artist_part = user_profile["favorite_artists"][0]

    if artist_part:
        return f"{mood} {artist_part}"
    return mood