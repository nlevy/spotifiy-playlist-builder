# Spotify Playlist Creator

A Flask web application that creates Spotify playlists from your favorite artists' top tracks.

## Setup

### Development Environment

1. Create and activate virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate on Unix/macOS
source .venv/bin/activate
# OR on Windows
.venv\Scripts\activate
```

2. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

3. Configure the application:
   - Create `.env` with your Spotify credentials:

```yaml
SECRET_KEY="your-secret-key"
SPOTIFY_CLIENT_KEY="your-spotify-client-id"
SPOTIFY_CLIENT_SECRET="your-spotify-client-secret"
SPOTIFY_REDIRECT_URI="http://127.0.0.1:5000/callback"
```

4. Run development server:

```bash
python run_dev.py
```

The app will be available at `http://127.0.0.1:5000`

### Production Environment

1. Set environment variables:

```bash
# Required environment variables
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
export SPOTIFY_CLIENT_KEY=your-spotify-client-id
export SPOTIFY_CLIENT_SECRET=your-spotify-client-secret
export SPOTIFY_REDIRECT_URI=https://your-domain.com/callback
```

2. Install production dependencies:

```bash
pip install -r requirements.txt
```

3. Run with Gunicorn:

```bash
# Basic usage
gunicorn -w 4 -b 0.0.0.0:8000 run_prod:app

# Or using the config file for more options
gunicorn -c gunicorn_config.py run_prod:app
```

The app will be available at `http://0.0.0.0:8000`

Note: For actual production deployment, you should:

- Use a reverse proxy (like Nginx) in front of Gunicorn
- Set up SSL/TLS
- Configure proper logging
- Use a process manager (like systemd or supervisor)

## Features

- OAuth authentication with Spotify
- View your top artists
- Create playlists with configurable number of top tracks per artist

## Project Structure

```
├── app/
│   ├── __init__.py        # Flask app initialization
│   │ config.py            # Configuration management
│   ├── routes/
│   │   ├── artists.py     # Artist listing routes
│   │   ├── auth.py        # Authentication routes
│   │   └── playlists.py   # Playlist creation routes
│   └── templates/         # HTML templates
├── run_dev.py             # Development server
└── run_prod.py            # Production server
```
