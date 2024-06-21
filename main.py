from utilities import debug_print
from reddit import get_random_text_from_reddit
import moviepy.editor as moviepy
from gtts import gTTS
from mutagen.mp3 import MP3


def main():
    text = get_random_text_from_reddit()
    debug_print(text)
    google_text_to_speech(text)
    audio = MP3("output_sound.mp3")
    duration = audio.info.length

    example_video(duration)


def google_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output_sound.mp3")


def example_video(duration):
    clip = moviepy.VideoFileClip("gameplay_footage/subway_surfers.mp4")
    subclip = clip.subclip(20, 20 + duration)

    #txt_clip = moviepy.TextClip(text, fontsize=20, color='white')
    #txt_clip = txt_clip.set_position(("center", "center")).set_duration(10)

    #final_clip = moviepy.CompositeVideoClip([subclip, txt_clip])
    final_clip = subclip.set_audio(moviepy.AudioFileClip("output_sound.mp3"))
    final_clip.write_videofile("output_video.mp4")


# Call the main function
main()
