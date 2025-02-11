import spotipy
from flask import render_template, redirect, url_for, session, request

from app import app
from app.spotify import logged_in


@app.route('/')
def bands():
    if not logged_in():
        return redirect(url_for('login', next=request.url))

    time_range = request.args.get('time_range','long_term')
    spotify_api = spotipy.Spotify(auth=session['token_info']['access_token'])
    resp = spotify_api.current_user_top_artists(time_range=time_range, limit=21)
    bands = resp['items']
    return render_template('bands.html', bands=bands) 