from utilities import debug_print, init_random_seed
import program_settings
from reddit import get_random_text_from_reddit
import text_to_speech as tts
import os
from mutagen.mp3 import MP3
import random


def main():
    init_random_seed()

    text = get_random_text_from_reddit()
    debug_print("Selected Text:\n" + text)

    debug_print("Creating text to speech with TikTok, this may take a while, please wait..." if program_settings.text_to_speech_settings["is_tiktok"]
                else "Creating text to speech with Google, this may take a while, please wait...")
    tts.create_text_to_speech(text)

    audio = MP3(program_settings.text_to_speech_settings["output_sound_file_path"])
    tts_duration = audio.info.length

    debug_print(f"Text to speech file created with the duration of {tts_duration} seconds")

    create_video(text, tts_duration)


def select_random_video():
    gameplay_footage_path = program_settings.program_settings["gameplay_footage_path"]

    # Find game folders
    all_game_folders = os.listdir(gameplay_footage_path)
    game_folders = []
    for game_folder in all_game_folders:
        if os.path.isdir(os.path.join(gameplay_footage_path, game_folder)):
            game_folders.append(game_folder)

    if not game_folders:
        raise ValueError("No game folders found")

    debug_print(f"Found {len(game_folders)} game folders")

    # Select a random game folder
    random_folder = random.choice(game_folders)
    random_folder_path = os.path.join(gameplay_footage_path, random_folder)

    debug_print(f"Selected game: {random_folder}")

    # Find videos in the selected game folder
    all_videos = os.listdir(random_folder_path)
    videos = []
    for video in all_videos:
        if os.path.isfile(os.path.join(random_folder_path, video)):
            videos.append(video)

    if not videos:
        raise ValueError(f"No videos found in the folder {random_folder}.")

    # Select a random video
    random_video = random.choice(videos)
    random_video_path = os.path.join(random_folder_path, random_video)
    debug_print(f"Selected random video: {random_video}")

    return random_video_path


def create_video(text, tts_duration):
    video_path = select_random_video()


# Call the main function
# main()

create_video("", 0)
