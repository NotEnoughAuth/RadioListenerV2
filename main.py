import json
import time

from DownloadAudio import DownloadAudio
from RequestAudio import RequestAudio
from SpotifyPlaylist import SpotifyPlaylist

while True:
    audio = DownloadAudio()
    request = RequestAudio()
    sp = SpotifyPlaylist()
    if not request.error:
        if not request.checkforrepeats('wmRadioSongList'):
            request.savedata('wmRadioSongList')
            sp.add_song(request.artist, request.title)
    sp.purge_songs('wmRadioSongList')
    time.sleep(60)
