import json

from DownloadAudio import DownloadAudio
from RequestAudio import RequestAudio
from SpotifyPlaylist import SpotifyPlaylist

while True:
    audio = DownloadAudio()
    request = RequestAudio()
    if not request.checkforrepeats('wmRadioSongList'):
        request.savedata('wmRadioSongList')
        sp = SpotifyPlaylist()
        sp.add_song(request.artist, request.title)


