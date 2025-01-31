import spotipy
from flask import render_template, redirect, url_for, request, session

from app import app
from app.logger import logger
from app.spotify import logged_in


@app.route('/create', methods=['GET', 'POST'])
def create():
    if not logged_in():
        return redirect(url_for('login', next=request.url))
        
    if request.method == 'POST':
        spotify_api = spotipy.Spotify(auth=session['token_info']['access_token'])
        playlist_name = request.form.get('playlist_name')
        artists = request.form.getlist('artists[]')
        songs_per_artist = int(request.form.get('songs_per_artist', 5))
        
        # Get user ID and create playlist
        user_info = spotify_api.current_user()
        logger.debug(f"Creating playlist '{playlist_name}' for user {user_info['id']}")
        playlist = spotify_api.user_playlist_create(
            user_info['id'],
            playlist_name,
            public=True,
            description=f"Playlist created with top {songs_per_artist} tracks from selected artists"
        )
        logger.debug(f"Created playlist: {playlist['name']} (id: {playlist['id']})")
        
        # Collect all track IDs
        track_ids = []
        
        for artist_name in artists:
            # Search for the artist
            logger.debug(f"Searching for artist: '{artist_name}'")
            results = spotify_api.search(q=artist_name, type='artist', limit=1)
            if not results['artists']['items']:
                logger.debug(f"Artist not found: {artist_name}")
                continue
                
            artist = results['artists']['items'][0]
            logger.debug(f"Found artist: {artist['name']} (id: {artist['id']})")
            
            # Get their top tracks
            logger.debug(f"Getting top tracks for {artist['name']}")
            logger.debug(f"API call: artist_top_tracks(artist_id='{artist['id']}')")
            top_tracks = spotify_api.artist_top_tracks(artist['id'])
            
            logger.debug(f"Top {songs_per_artist} tracks:")
            for i, track in enumerate(top_tracks['tracks'][:songs_per_artist]):
                logger.debug(f"{i+1}. {track['name']} (id: {track['id']})")
                track_ids.append(track['id'])
        
        # Add all tracks to playlist
        if track_ids:
            logger.debug(f"Adding {len(track_ids)} tracks to playlist")
            spotify_api.playlist_add_items(playlist['id'], track_ids)
            logger.debug("Successfully added tracks to playlist")
            
            # Get the playlist URL for redirection
            playlist_url = playlist['external_urls']['spotify']
            logger.debug(f"Playlist URL: {playlist_url}")
            
            return render_template('playlist_created.html',
                                playlist_name=playlist_name,
                                track_count=len(track_ids),
                                playlist_url=playlist_url)
        else:
            logger.debug("No tracks were found to add to the playlist")
            # Could add an error message here
            return redirect(url_for('create'))
        
    return render_template('create_playlist.html') 