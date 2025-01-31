from urllib.parse import urlencode

from flask import redirect, request, session, url_for

from app import app
from app.spotify import create_spotify_oauth


@app.route('/login')
def login():
    sp_oauth = create_spotify_oauth()
    next_url = request.args.get('next')
    auth_url = sp_oauth.get_authorize_url() + '&' + urlencode({'next': next_url})
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = create_spotify_oauth()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info

    next_url = request.args.get('next')
    if next_url:
        return redirect(next_url)
    return redirect(url_for('bands')) 