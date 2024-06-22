from utilities import debug_print
import program_settings
from reddit import get_random_text_from_reddit
import text_to_speech as tts

import moviepy.editor as moviepy
from mutagen.mp3 import MP3


def main():
    text = get_random_text_from_reddit()
    debug_print("Selected Text:\n" + text)

    debug_print("Creating text to speech with TikTok, this may take a while, please wait..." if program_settings.text_to_speech_settings["is_tiktok"]
                else "Creating text to speech with Google, this may take a while, please wait...")
    tts.create_text_to_speech(text)

    audio = MP3(program_settings.text_to_speech_settings["output_sound_file_path"])
    duration = audio.info.length

    debug_print(f"Text to speech file created with the duration of {duration} seconds")

    #example_video(duration)


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
