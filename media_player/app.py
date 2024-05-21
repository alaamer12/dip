from audio import Audio, AudioPlayer
from video import Video, VideoPlayer

def main():
    audio = Audio()
    audio_player = AudioPlayer(audio)
    audio_player.play_audio()

    video = Video()
    video_player = VideoPlayer(video)
    video_player.play_video()

if __name__ == "__main__":
    main()
