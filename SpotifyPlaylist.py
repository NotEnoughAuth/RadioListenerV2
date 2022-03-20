import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import requests


class SpotifyPlaylist:
    BASE_URL = 'https://api.spotify.com/v1/'
    PLAYLIST_ID = '2uHhH7dnaVxZS988Ld0XSp'
    USERNAME = 'minecraftmagic05'
    access_token = None
    headers = None
    spotifyObject = None

    def __init__(self):
        CLIENT_ID = '1ab0a158c446421fa9c5d32942d7108e'
        CLIENT_SECRET = '05fef8dacc34404c9282e50ed7800808'
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        scope = ['playlist-modify', 'user-read-private']

        token = SpotifyOAuth(scope=scope, username=self.USERNAME, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:8888')
        self.spotifyObject = spotipy.Spotify(auth_manager=token)

    def add_song(self, artist, title):
        stupidlist = []
        stupidlist.append(self.search_song(artist, title))
        print(stupidlist)
        self.spotifyObject.playlist_add_items(playlist_id=self.PLAYLIST_ID, items=stupidlist)

    def search_song(self, artist, title):
        print(artist + ' ' + title)
        r = self.spotifyObject.search(q=title + ' ' + artist, type='track')
        print(r['tracks']['items'][0]['uri'])
        return r['tracks']['items'][0]['uri']
