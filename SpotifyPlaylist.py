import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests


class SpotifyPlaylist:
    BASE_URL = 'https://api.spotify.com/v1/'
    PLAYLIST_ID = '2uHhH7dnaVxZS988Ld0XSp'
    access_token = None
    headers = None

    def __init__(self):
        CLIENT_ID = '1ab0a158c446421fa9c5d32942d7108e'
        CLIENT_SECRET = '05fef8dacc34404c9282e50ed7800808'
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'authorization_code',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })

        auth_response_data = auth_response.json()

        self.access_token = auth_response_data['access_token']

        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }

    def add_song(self, artist, title):
        songid = self.search_song(artist, title)
        r = requests.post(self.BASE_URL + 'playlists/' + self.PLAYLIST_ID + '/tracks?quris=spotify:track:' + songid, headers=self.headers)
        return r

    def search_song(self, artist, title):
        # make spaces in the artist into + so you can narrow down the correct uri
        r = requests.get(self.BASE_URL + 'search?q=artist:' + artist + '&type=track', headers=self.headers)
        r = r.json()
        r = json.dumps(r)
        r = json.loads(r)
        return r['tracks']['items'][0]['id']
