import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')

    # Spotify configuration
    SPOTIFY_CLIENT_KEY = os.getenv('SPOTIFY_CLIENT_KEY')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

    def __init__(self):
        # Validate required settings
        required = ['SPOTIFY_CLIENT_KEY', 'SPOTIFY_CLIENT_SECRET', 'SPOTIFY_REDIRECT_URI']
        missing = [key for key in required if not getattr(self, key)]
        if missing:
            raise ValueError(f"Missing required configuration: {', '.join(missing)}")

    @staticmethod
    def init_app(app):
        pass

