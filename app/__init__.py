from flask import Flask

app = Flask(__name__)

# Import routes after app creation to avoid circular imports
from app.routes import auth, playlists, artists 