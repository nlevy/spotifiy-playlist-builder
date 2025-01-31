import time

from flask import session
from spotipy.oauth2 import SpotifyOAuth

from app.config import Config


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=Config.SPOTIFY_CLIENT_KEY,
        client_secret=Config.SPOTIFY_CLIENT_SECRET,
        redirect_uri=Config.SPOTIFY_REDIRECT_URI,
        scope="user-read-private user-read-email user-top-read playlist-modify-public playlist-modify-private",
        show_dialog=True,
        cache_path='token.txt'
    )

def logged_in():
    return 'token_info' in session and session['token_info']['expires_at'] > time.time()
