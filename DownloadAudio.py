import requests
from pathlib import Path
from os import path
from pydub import AudioSegment


class DownloadAudio:
    url = "https://retail-music.com/walmart_radio.mp3"
    size = 2e5
    p = None

    def __init__(self):
        r = requests.get(self.url, stream=True)
        sectors = self.size / 9
        repeat = 1
        with open('wmRadio.mp3', 'wb') as f:
            print("Downloading File", end="")
            for chunk in r.iter_content(32 * 1024):
                f.write(chunk)
                path = Path("wmRadio.mp3")
                self.p = path
                if path.stat().st_size > (sectors * repeat):
                    repeat += 1
                    print(".", end="")

                if path.stat().st_size > self.size:
                    print(".")
                    break

    def path(self):
        return self.p

    def mp3_to_wav(self):
        if self.p is None:
            print("You need to download the audio before you format it")
            pass

        audio = AudioSegment.from_mp3(self.p)
        audio.export("wmRadio.raw", format="raw")
        return "Audio has been formatted!"
