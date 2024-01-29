'''
Creates a spotify playlist for your top songs in a given period
Naming convention is 'Your Top Songs'

Usage:
1) Set up Spotify Developer API for your account
2) Make the modifications for your personal account data below
3) Enjoy the list of your favorite recent songs

Modifications:
    SPOTIFY_CLIENT_ID
    SPOTIFY_CLIENT_SECRET
    SPOTIFY_REDIRECT_URI
    SPOTIFY_USERNAME
    SPOTIFY_RANGE

SPOTIFY_RANGE values:
    short-term      = Last 4 weeks
    medium_term     = Last 6 months
    long_term       = All time
'''


from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


# Constants for use with Spotipy API
SPOTIFY_CLIENT_ID = "REDACTED"
SPOTIFY_CLIENT_SECRET = "REDACTED"
SPOTIFY_REDIRECT_URI = "REDACTED"
SPOTIFY_USERNAME = "REDACTED"
SPOTIFY_RANGE = 'long_term'


def get_top_songs():
    '''
    Uses spotipy.Spotify to query your top 50 (max number) of songs for a given period.

    param: SPOTIFY_RANGE
      short-term     = Last 4 weeks
      medium_term    = Last 6 months
      long_term      = All time
    return: List of song URIs for use with Spotify API
    '''
    sp = Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                client_secret=SPOTIFY_CLIENT_SECRET,
                                                redirect_uri=SPOTIFY_REDIRECT_URI,
                                                scope='user-top-read'))

    top_tracks = sp.current_user_top_tracks(time_range=SPOTIFY_RANGE, limit=50)
    song_uris = [item['uri'] for item in top_tracks['items']]
    return song_uris


def add_spotify_playlist(song_uris):
    '''
    Creates a Spotify playlist with the input list generated from get_playlist().

    param input_list: List of 100 song/artist tuple pairs.
    param year: The year of the playlist in format 'YYYY'.
    '''
    sp = Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=SPOTIFY_REDIRECT_URI,
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username=SPOTIFY_USERNAME
        )
    )
    user_id = sp.current_user()["id"]

    playlist_name = "Your Top Songs"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


def main():
    '''
    Main function that takes query years and processes them through playlist lookup and creation.

    param billboard_years: List of years in format 'YYYY-MM-DD'.
    '''
    song_uri_list = get_top_songs()
    add_spotify_playlist(song_uri_list)


if __name__ == '__main__':
    main()
