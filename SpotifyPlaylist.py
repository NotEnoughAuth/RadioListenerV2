import json
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import requests


class SpotifyPlaylist:
    BASE_URL = 'https://api.spotify.com/v1/'
    PLAYLIST_ID = 'PLAYLIST_ID'
    USERNAME = 'USERNAME'
    access_token = None
    headers = None
    spotifyObject = None

    def __init__(self):
        CLIENT_ID = 'CLIENT_ID'
        CLIENT_SECRET = 'CLIENT+SECRET'
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        scope = ['playlist-modify', 'user-read-private']

        token = SpotifyOAuth(scope=scope, username=self.USERNAME, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:8888')
        self.spotifyObject = spotipy.Spotify(auth_manager=token)

    def add_song(self, artist, title):
        stupidlist = [self.search_song(artist, title)]
        print(stupidlist)
        self.spotifyObject.playlist_add_items(playlist_id=self.PLAYLIST_ID, items=stupidlist)

    def search_song(self, artist, title):
        print(artist + ' ' + title)
        try:
            r = self.spotifyObject.search(q=title + ' ' + artist, type='track')
            print(r['tracks']['items'][0]['uri'])
            return r['tracks']['items'][0]['uri']
        except:
            print('Error could not find spotify uri removing from file')


    def purge_songs(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            sections = line.split('\t')
            songtime = datetime.datetime.strptime(sections[0], "%Y-%m-%d %H:%M:%S")
            if songtime - datetime.datetime.now() > datetime.timedelta(1):
                self.remove_song(sections[2], sections[1])
            else:
                f.write(line)

    def remove_song(self, artist, title):
        stupidlist = [self.search_song(artist, title)]
        print(f'Removing {title} By: {artist}')
        self.spotifyObject.playlist_remove_all_occurrences_of_items(self.PLAYLIST_ID, stupidlist)

    def remove_from_file(self, artist, title, filepath):
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
            for line in lines:
                if line.__contains__(title + '\t' + artist + '\n'):
                    print(f'DELETED {title} BY: {artist} FROM FILE')
        except FileNotFoundError:
            print('Error File Not Found')
            