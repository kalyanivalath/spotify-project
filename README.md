# Spotify Weather Playlist Recommender

A web application that generates Spotify playlists based on current weather conditions in a given location.

## Overview
This project connects the Spotify Web API and OpenWeather API to generate playlists that match the mood of the weather. The application fetches real-time weather data and maps weather conditions to music moods.

Example:
- Sunny → upbeat pop
- Rainy → mellow acoustic
- Snowy → calm ambient

## Features
- Fetch real-time weather data
- Map weather conditions to music moods
- Generate Spotify playlists dynamically
- Display songs with album artwork

## Tech Stack
Frontend:
- HTML
- CSS
- JavaScript (or React)

Backend:
- Python (Flask or FastAPI)

APIs:
- Spotify Web API
- OpenWeather API

## Setup

1. Clone the repository

git clone https://github.com/YOURUSERNAME/spotify-weather-playlist.git

2. Install dependencies

pip install -r requirements.txt

3. Add environment variables

Create a `.env` file

SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
OPENWEATHER_API_KEY=

4. Run the app

python app.py

## Future Improvements
- Personalized recommendations based on user listening history
- Better weather-to-mood ML model
- Mobile-friendly UI
- Save generated playlists to Spotify account

## Notes for me
- next add a place to enter city to check weather for the city they are in
- next make the reccommendations actually personalized to the user
- next make sure /callback redirects back to the frontend page
- next fix recommendation logic the issue is either with spotify login and token scope or with the request endpoint try to test with postman next

## Author
Kalyani Valath
