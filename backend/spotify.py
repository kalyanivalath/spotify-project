import os
import base64
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")


def get_login_url():
    scope = "user-read-private user-read-email"

    params = {
        "client_id": SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "scope": scope
    }

    return "https://accounts.spotify.com/authorize?" + urlencode(params)


def get_token(code):
    auth_string = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": SPOTIFY_REDIRECT_URI
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def search_tracks(access_token, query, limit=10):
    url = "https://api.spotify.com/v1/search"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "q": query,
        "type": "track",
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_top_tracks(access_token, limit=10, time_range="medium_term"):
    url = "https://api.spotify.com/v1/me/top/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "limit": limit,
        "time_range": time_range
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_top_artists(access_token, limit=10, time_range="medium_term"):
    url = "https://api.spotify.com/v1/me/top/artists"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "limit": limit,
        "time_range": time_range
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_recently_played(access_token, limit=10):
    url = "https://api.spotify.com/v1/me/player/recently-played"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_saved_tracks(access_token, limit=10):
    url = "https://api.spotify.com/v1/me/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()