from datetime import datetime, timedelta
from acrcloud.recognizer import ACRCloudRecognizer
import json


class RequestAudio:
    artist = None
    title = None

    def __init__(self):
        config = {
            'host': 'HOST_SERVER',
            'access_key': 'ACCESS_KEY',
            'access_secret': 'ACCESS_SECRET',
            'debug': True,
            'timeout': 10
        }

        acrcloud = ACRCloudRecognizer(config)

        data = acrcloud.recognize_by_file('wmRadio.mp3', 0)

        j = json.loads(data)

        self.artist = (j['metadata']['music'][0]['artists'][0]['name'])
        self.title = (j['metadata']['music'][0]['title'])

    def savedata(self, filepath):
        file = open(filepath, 'a')
        file.write(f'{datetime.now()}\t{self.title}\t{self.artist}\n')
        file.close()

    def checkforrepeats(self, filepath):
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
            for line in lines:
                if line.__contains__(self.title + '\t' + self.artist + '\n'):
                    return True
        except FileNotFoundError:
            return False

    def artist(self):
        return self.artist

    def title(self):
        return self.title
