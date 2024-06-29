from utilities import debug_print, init_random_seed
import program_settings
from reddit import get_random_text_from_reddit
import text_to_speech as tts
import os
from mutagen.mp3 import MP3
import moviepy.editor
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


def select_random_video(folder_path=None):
    if not folder_path:
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

    else:
        if not os.path.isdir(folder_path):
            raise ValueError(f"The given folder path {folder_path} is not a valid folder path.")

        random_folder_path = folder_path
        random_folder = os.path.basename(random_folder_path)
        debug_print(f"Folder path is given, selected game is {random_folder}.")

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

    return random_video_path, random_folder_path


def create_video(text, tts_duration):
    video_path, folder_path = select_random_video()
    video = moviepy.editor.VideoFileClip(video_path)

    videos = [video]
    video_durations = [video.duration]
    total_video_duration = video.duration

    while_loop_counter = 0

    # We will merge videos until the duration of the text-to-speech is shorter than the duration of the all videos
    while tts_duration > total_video_duration:
        debug_print("Duration of the selected videos are shorter than the text-to-speech duration, selecting and adding another video.")
        while_loop_counter += 1
        if while_loop_counter > program_settings.program_settings["max_while_loop_count_for_video_selection"]:
            raise ValueError("Maximum while loop count reached, could not find a video to cover the text-to-speech duration. "
                             "Add more videos or allow same video selection.")

        video_path, _ = select_random_video(folder_path)
        video = moviepy.editor.VideoFileClip(video_path)

        same_video_while_loop_counter = 0
        # If selected video is selected again, select another video
        if not program_settings.program_settings["allow_same_video_selection"]:
            while has_video_in_videos(video, videos):
                same_video_while_loop_counter += 1
                if same_video_while_loop_counter > program_settings.program_settings["max_while_loop_count_for_video_selection"]:
                    raise ValueError("Maximum while loop count reached, could not find a video to cover the text-to-speech duration. "
                                     "Add more videos or allow same video selection.")

                debug_print("Selected video is selected again, selecting another video.")
                video_path, _ = select_random_video(folder_path)
                video = moviepy.editor.VideoFileClip(video_path)

        videos.append(video)
        video_durations.append(video.duration)

        total_video_duration += video.duration

    debug_print(f"Selected {len(videos)} videos which have a total duration of {total_video_duration} seconds")

    # Select random start time
    start_time = random.uniform(0, total_video_duration - tts_duration)
    end_time = start_time + tts_duration

    debug_print(f"Selected start time: {start_time}, end time: {end_time}")

    # Find the first video according to start_time, it doesn't have to be the first video in the list
    current_time = 0
    first_video_index = 0
    for i, duration in enumerate(video_durations):
        if current_time + duration > start_time:
            first_video_index = i
            break
        current_time += duration

    first_video = videos[first_video_index]
    last_video = videos[-1]

    debug_print(f"First video is: {first_video.filename}, last video is: {last_video.filename}")

    # Find the start time in the first video
    start_time_in_first_video = start_time - current_time  # Current time is the length of the videos before the first video at this point
    debug_print(f"Start time in the first video: {start_time_in_first_video}")

    # Find the end time in the last video, last video has to be the last video in the list
    current_time = 0
    end_time_in_last_video = 0
    for i, duration in enumerate(video_durations):
        if current_time + duration > end_time:
            end_time_in_last_video = end_time - current_time  # Current time is the length of the videos before the first video at this point
            break
        current_time += duration

    debug_print(f"End time in the last video: {end_time_in_last_video}")

    # Trim the first and last videos
    first_video = first_video.subclip(start_time_in_first_video, first_video.duration)
    last_video = last_video.subclip(0, end_time_in_last_video)

    # Trim the videos between the first and last videos
    videos = videos[first_video_index + 1:]
    videos = videos[:-1]

    for i, video in enumerate(videos):
        videos[i] = video.subclip(0, video.duration)

    # Concatenate the videos
    final_video = moviepy.editor.concatenate_videoclips([first_video] + videos + [last_video])
    debug_print(f"Final video duration: {final_video.duration} seconds")

    # Add sound to the final video
    audio = moviepy.editor.AudioFileClip(program_settings.text_to_speech_settings["output_sound_file_path"])
    final_video = final_video.set_audio(audio)

    if os.path.exists(program_settings.program_settings["output_video_path"]):
        os.remove(program_settings.program_settings["output_video_path"])

    final_video.write_videofile(program_settings.program_settings["output_video_path"])


def has_video_in_videos(video, videos):
    for v in videos:
        if v.filename == video.filename:
            return True
    return False


# Call the main function
main()
