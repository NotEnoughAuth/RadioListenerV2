import json

from DownloadAudio import DownloadAudio
from RequestAudio import RequestAudio
from SpotifyPlaylist import SpotifyPlaylist

# audio = DownloadAudio()
request = RequestAudio()
request.savedata('wmRadioSongList')

sp = SpotifyPlaylist()
r = sp.add_song(request.artist, request.title)
print(r)
r = r.json()
r = json.dumps(r)
y = json.loads(r)
print(y)


