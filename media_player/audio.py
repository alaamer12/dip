from media import Media

class Audio(Media):
    def play(self):
        print("Playing audio")

class AudioPlayer:
    def __init__(self, audio: Audio):
        self.audio = audio

    def play_audio(self):
        self.audio.play()
