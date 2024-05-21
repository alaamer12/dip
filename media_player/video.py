from media import Media

class Video(Media):
    def play(self):
        print("Playing video")

class VideoPlayer:
    def __init__(self, video: Video):
        self.video = video

    def play_video(self):
        self.video.play()
